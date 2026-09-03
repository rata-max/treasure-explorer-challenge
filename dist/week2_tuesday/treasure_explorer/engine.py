from __future__ import annotations

from dataclasses import dataclass

from .model import Action, Observation, TreasureInfo

MOVE = {
    Action.MOVE_UP: (-1, 0), Action.MOVE_DOWN: (1, 0),
    Action.MOVE_LEFT: (0, -1), Action.MOVE_RIGHT: (0, 1),
}
TERRAIN_COST = {".": 1, "S": 1, "E": 1, "T": 1, "M": 4, "W": 7}


@dataclass(frozen=True)
class GameSpec:
    grid: tuple[str, ...]
    energy: int
    treasures: dict[tuple[int, int], int]
    visibility: str = "public"  # public | local
    reveal_radius: int = 1
    hidden_values: bool = False
    exit_bonus: int = 50
    max_turns: int = 500


class Game:
    def __init__(self, spec: GameSpec):
        self.spec = spec
        self.start = self._find("S")
        self.exit = self._find("E")
        self.position = self.start
        self.energy = spec.energy
        self.turn = 0
        self.collected: set[tuple[int, int]] = set()
        self.discovered_values: set[tuple[int, int]] = set()
        self.revealed: set[tuple[int, int]] = set()
        self.invalid_actions = 0
        self.exited = False
        self.history: list[dict] = []
        self._reveal()

    def _find(self, symbol: str) -> tuple[int, int]:
        found = [(r, c) for r, row in enumerate(self.spec.grid) for c, tile in enumerate(row) if tile == symbol]
        if len(found) != 1:
            raise ValueError(f"map must contain exactly one {symbol}")
        return found[0]

    def _reveal(self) -> None:
        if self.spec.visibility == "public":
            self.revealed = {(r, c) for r, row in enumerate(self.spec.grid) for c in range(len(row))}
        else:
            r0, c0 = self.position
            for r, row in enumerate(self.spec.grid):
                for c in range(len(row)):
                    if abs(r-r0) + abs(c-c0) <= self.spec.reveal_radius:
                        self.revealed.add((r, c))
        if self.position in self.spec.treasures:
            self.discovered_values.add(self.position)

    def observation(self) -> Observation:
        shown = []
        for r, row in enumerate(self.spec.grid):
            shown.append("".join(tile if (r, c) in self.revealed else "?" for c, tile in enumerate(row)))
        treasures = tuple(
            TreasureInfo(pos, value if not self.spec.hidden_values or pos in self.discovered_values else None,
                         pos in self.collected)
            for pos, value in sorted(self.spec.treasures.items())
            if self.spec.visibility == "public" or pos in self.revealed
        )
        visible_exit = self.exit if self.spec.visibility == "public" or self.exit in self.revealed else None
        return Observation(self.turn, self.position, visible_exit, self.energy, tuple(shown), treasures)

    def step(self, raw_action: Action | str) -> None:
        before = self.position
        try:
            action = raw_action if isinstance(raw_action, Action) else Action(raw_action)
        except (ValueError, TypeError):
            action = None
        if action == Action.COLLECT:
            if self.position in self.spec.treasures and self.position not in self.collected and self.energy >= 1:
                self.energy -= 1
                self.collected.add(self.position)
            else:
                self.invalid_actions += 1
        elif action in MOVE:
            dr, dc = MOVE[action]
            nr, nc = self.position[0] + dr, self.position[1] + dc
            valid = 0 <= nr < len(self.spec.grid) and 0 <= nc < len(self.spec.grid[0])
            if valid and self.spec.grid[nr][nc] != "#" and self.energy >= TERRAIN_COST[self.spec.grid[nr][nc]]:
                self.energy -= TERRAIN_COST[self.spec.grid[nr][nc]]
                self.position = (nr, nc)
                self._reveal()
                self.exited = self.position == self.exit
            else:
                self.invalid_actions += 1
        else:
            self.invalid_actions += 1
        self.history.append({"turn": self.turn, "from": before, "to": self.position,
                             "action": str(action), "energy": self.energy})
        self.turn += 1

    @property
    def done(self) -> bool:
        return self.exited or self.energy <= 0 or self.turn >= self.spec.max_turns

    def result(self) -> dict:
        treasure = sum(self.spec.treasures[p] for p in self.collected)
        score = self.spec.exit_bonus + treasure + self.energy - 5*self.invalid_actions if self.exited else 0
        return {"score": score, "exited": self.exited, "treasure_value": treasure,
                "remaining_energy": self.energy, "invalid_actions": self.invalid_actions,
                "turns": self.turn}

