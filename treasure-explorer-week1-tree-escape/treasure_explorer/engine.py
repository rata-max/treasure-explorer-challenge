from __future__ import annotations

from dataclasses import dataclass

from .model import Action, ItemInfo, Observation, TreasureInfo

MOVE = {
    Action.MOVE_UP: (-1, 0),
    Action.MOVE_DOWN: (1, 0),
    Action.MOVE_LEFT: (0, -1),
    Action.MOVE_RIGHT: (0, 1),
}
COST = {".": 1, "S": 1, "E": 1, "T": 1, "K": 1, "B": 1, "M": 4, "W": 5}


@dataclass(frozen=True)
class GameSpec:
    grid: tuple[str, ...]
    energy: int
    treasures: dict[tuple[int, int], int]
    items: dict[tuple[int, int], str] | None = None
    battery_gain: int = 8
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
        self.collected_items: set[tuple[int, int]] = set()
        self.has_key = False
        self.discovered_values: set[tuple[int, int]] = set()
        self.revealed: set[tuple[int, int]] = set()
        self.invalid_actions = 0
        self.exited = False
        self._reveal_nearby()

    def _find(self, symbol: str) -> tuple[int, int]:
        found = [(r, c) for r, row in enumerate(self.spec.grid) for c, x in enumerate(row) if x == symbol]
        if len(found) != 1:
            raise ValueError(f"map must contain exactly one {symbol}")
        return found[0]

    def _reveal_nearby(self) -> None:
        r, c = self.position
        for dr, dc in ((0, 0), (-1, 0), (1, 0), (0, -1), (0, 1)):
            q = (r + dr, c + dc)
            if 0 <= q[0] < len(self.spec.grid) and 0 <= q[1] < len(self.spec.grid[0]):
                self.revealed.add(q)
        if self.position in self.spec.treasures:
            self.discovered_values.add(self.position)

    def observation(self) -> Observation:
        rows = []
        for r, row in enumerate(self.spec.grid):
            shown = []
            for c, tile in enumerate(row):
                if tile in "MW" and (r, c) not in self.revealed:
                    shown.append("?")
                else:
                    shown.append(tile)
            rows.append("".join(shown))
        treasures = tuple(
            TreasureInfo(p, value if p in self.discovered_values else None, p in self.collected)
            for p, value in sorted(self.spec.treasures.items())
        )
        items = tuple(
            ItemInfo(p, kind, p in self.collected_items)
            for p, kind in sorted((self.spec.items or {}).items())
        )
        return Observation(self.turn, self.position, self.exit, self.energy, tuple(rows), treasures, items, self.has_key)

    def _collect_item(self) -> None:
        items = self.spec.items or {}
        if self.position not in items or self.position in self.collected_items:
            return
        self.collected_items.add(self.position)
        if items[self.position] == "key":
            self.has_key = True
        elif items[self.position] == "battery":
            self.energy += self.spec.battery_gain

    def step(self, raw_action: Action | str) -> None:
        try:
            action = raw_action if isinstance(raw_action, Action) else Action(raw_action)
        except (ValueError, TypeError):
            self.invalid_actions += 1
            self.turn += 1
            return

        if action == Action.COLLECT:
            if self.position not in self.spec.treasures or self.position in self.collected or self.energy < 1:
                self.invalid_actions += 1
            else:
                self.energy -= 1
                self.collected.add(self.position)
        else:
            dr, dc = MOVE[action]
            nr, nc = self.position[0] + dr, self.position[1] + dc
            valid = 0 <= nr < len(self.spec.grid) and 0 <= nc < len(self.spec.grid[0])
            if not valid or self.spec.grid[nr][nc] == "#":
                self.invalid_actions += 1
            else:
                cost = COST[self.spec.grid[nr][nc]]
                if self.energy < cost:
                    self.invalid_actions += 1
                else:
                    self.energy -= cost
                    self.position = (nr, nc)
                    self._collect_item()
                    self._reveal_nearby()
                    key_required = any(kind == "key" for kind in (self.spec.items or {}).values())
                    self.exited = self.position == self.exit and (self.has_key or not key_required)
        self.turn += 1

    @property
    def done(self) -> bool:
        return self.exited or self.energy <= 0 or self.turn >= self.spec.max_turns

    def result(self) -> dict[str, int | bool]:
        treasure_score = sum(self.spec.treasures[p] for p in self.collected)
        score = treasure_score + self.energy - 5 * self.invalid_actions if self.exited else 0
        return {
            "score": score,
            "exited": self.exited,
            "treasure_value": treasure_score,
            "remaining_energy": self.energy,
            "invalid_actions": self.invalid_actions,
            "turns": self.turn,
            "has_key": self.has_key,
            "items_collected": len(self.collected_items),
        }
