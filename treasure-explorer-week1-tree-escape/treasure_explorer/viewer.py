from __future__ import annotations

import os
import time


class TerminalViewer:
    """Dependency-free turn viewer for the Week 1 tree-maze assignment."""

    def __init__(self, delay: float = 0.15):
        self.delay = max(0.0, delay)

    def __call__(self, game, observation, action) -> None:
        if os.name == "nt":
            os.system("cls")
        else:
            print("\033[2J\033[H", end="")

        collected = game.collected_items
        for r, row in enumerate(observation.grid):
            rendered = []
            for c, tile in enumerate(row):
                pos = (r, c)
                if pos == observation.position:
                    rendered.append("A")
                elif pos in collected and tile in "KB":
                    rendered.append(".")
                else:
                    rendered.append(tile)
            print(" ".join(rendered))

        action_name = "DONE" if action is None else getattr(action, "value", str(action))
        print()
        print(f"turn={observation.turn:03d}  energy={observation.energy:03d}  action={action_name}")
        print(f"key={'YES' if observation.has_key else 'NO '}  items={len(collected)}  exit={game.exit}")
        print("Legend: A agent | K key | B battery | E exit | # wall")
        if self.delay:
            time.sleep(self.delay)
