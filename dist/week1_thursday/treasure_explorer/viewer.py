from __future__ import annotations

import os
import time


class TerminalViewer:
    """Dependency-free terminal animation for Treasure Explorer."""

    def __init__(self, delay: float = 0.20, clear: bool = True):
        self.delay = max(0.0, delay)
        self.clear = clear

    def __call__(self, game) -> None:
        if self.clear:
            if os.name == "nt":
                os.system("cls")
            else:
                print("\033[2J\033[H", end="")
        else:
            print("\n" + "=" * 46)

        obs = game.observation()
        for r, row in enumerate(obs.grid):
            rendered = []
            for c, tile in enumerate(row):
                pos = (r, c)
                if pos == obs.position:
                    rendered.append("A")
                elif pos in game.collected and tile == "T":
                    rendered.append(".")
                else:
                    rendered.append(tile)
            print(" ".join(rendered))

        last = game.history[-1] if game.history else None
        action = last["action"] if last else "START"
        treasure_value = sum(game.spec.treasures[p] for p in game.collected)
        print()
        print(
            f"turn={game.turn:03d}  energy={game.energy:03d}  "
            f"action={action}"
        )
        print(
            f"treasure={treasure_value:03d}  collected={len(game.collected)}  "
            f"invalid={game.invalid_actions}  exit={game.exit}"
        )
        print("Legend: A agent | T treasure | E exit | S start | # wall")
        if self.delay:
            time.sleep(self.delay)
