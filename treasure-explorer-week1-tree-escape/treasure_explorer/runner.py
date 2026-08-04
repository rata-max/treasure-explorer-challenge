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
    locations = {(r, c) for r, row in enumerate(grid) for c, x in enumerate(row) if x == "T"}
    treasures = {tuple(item["position"]): int(item["value"]) for item in data.get("treasures", [])}
    if locations != set(treasures):
        raise ValueError("T cells and treasure entries must match")
    item_symbols = {"K": "key", "B": "battery"}
    map_items = {
        (r, c): item_symbols[x]
        for r, row in enumerate(grid)
        for c, x in enumerate(row)
        if x in item_symbols
    }
    declared_items = {tuple(item["position"]): str(item["kind"]) for item in data.get("items", [])}
    if declared_items and declared_items != map_items:
        raise ValueError("K/B cells and item entries must match")
    items = declared_items or map_items
    return GameSpec(
        grid=grid,
        energy=int(data.get("energy", 100)),
        treasures=treasures,
        items=items,
        battery_gain=int(data.get("battery_gain", 8)),
        max_turns=int(data.get("max_turns", 500)),
    )


def load_agent(path: str | Path):
    spec = importlib.util.spec_from_file_location("student_agent", path)
    if spec is None or spec.loader is None:
        raise ValueError("cannot load agent")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    if not callable(getattr(module, "choose_action", None)):
        raise ValueError("agent.py must define choose_action(observation)")
    return module.choose_action


def run(map_path: str, agent_path: str, verbose: bool = False, observer=None) -> dict:
    game = Game(load_map(map_path))
    choose_action = load_agent(agent_path)
    while not game.done:
        obs = game.observation()
        action = choose_action(obs)
        if observer:
            observer(game, obs, action)
        if verbose:
            print(f"turn={obs.turn} pos={obs.position} energy={obs.energy} action={action}")
        game.step(action)
    if observer:
        observer(game, game.observation(), None)
    return game.result()
