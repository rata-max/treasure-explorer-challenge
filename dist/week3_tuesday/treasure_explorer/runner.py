from __future__ import annotations

import importlib.util
import json
from pathlib import Path

from .engine import Game, GameSpec


def load_map(path: str | Path) -> GameSpec:
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    grid = tuple(data["grid"])
    if not grid or len({len(row) for row in grid}) != 1:
        raise ValueError("grid must be a non-empty rectangle")
    if any(tile not in "#SET.MW" for row in grid for tile in row):
        raise ValueError("unknown tile")
    treasures = {tuple(x["position"]): int(x["value"]) for x in data.get("treasures", [])}
    cells = {(r, c) for r, row in enumerate(grid) for c, tile in enumerate(row) if tile == "T"}
    if cells != set(treasures):
        raise ValueError("T cells and treasure entries must match")
    return GameSpec(grid, int(data["energy"]), treasures, data.get("visibility", "public"),
                    int(data.get("reveal_radius", 1)), bool(data.get("hidden_values", False)),
                    int(data.get("exit_bonus", 50)), int(data.get("max_turns", 500)))


def load_agent(path: str | Path):
    spec = importlib.util.spec_from_file_location("student_agent", path)
    if not spec or not spec.loader:
        raise ValueError("cannot load agent")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    if not callable(getattr(module, "choose_action", None)):
        raise ValueError("agent.py must define choose_action(observation)")
    return module.choose_action


def run(map_path: str | Path, agent_path: str | Path, observer=None) -> tuple[dict, list[dict]]:
    game = Game(load_map(map_path))
    choose_action = load_agent(agent_path)
    while not game.done:
        obs = game.observation()
        game.step(choose_action(obs))
        if observer:
            observer(game)
    return game.result(), game.history

