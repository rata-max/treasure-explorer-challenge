"""Batch evaluation for the Week 3 final. DO NOT EDIT OR SUBMIT THIS FILE.

    python evaluate.py                    # public maps + generated seeds 0-49
    python evaluate.py --seeds 100-199    # another range of practice seeds
    python evaluate.py --maps-only        # only maps/*.json
    python evaluate.py --csv results.csv  # also write one row per run

Each run is independent (fresh state, turn 0), exactly like the private
evaluation, which uses unpublished seeds of treasure_explorer/generator.py.
"""

from __future__ import annotations

import argparse
import csv
import statistics
from pathlib import Path

from treasure_explorer.engine import Game, GameSpec
from treasure_explorer.generator import generate
from treasure_explorer.runner import load_agent, load_map

ROOT = Path(__file__).resolve().parent


def spec_from_dict(data: dict) -> GameSpec:
    return GameSpec(tuple(data["grid"]), int(data["energy"]),
                    {tuple(t["position"]): int(t["value"]) for t in data["treasures"]},
                    data.get("visibility", "local"), int(data.get("reveal_radius", 1)),
                    bool(data.get("hidden_values", True)), int(data.get("exit_bonus", 50)),
                    int(data.get("max_turns", 500)))


def play(spec: GameSpec, choose_action) -> dict:
    game = Game(spec)
    while not game.done:
        game.step(choose_action(game.observation()))
    return game.result()


def parse_range(text: str) -> range:
    lo, _, hi = text.partition("-")
    return range(int(lo), int(hi or lo) + 1)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--agent", default=str(ROOT / "agent.py"))
    parser.add_argument("--seeds", default="0-49")
    parser.add_argument("--maps-only", action="store_true")
    parser.add_argument("--csv")
    args = parser.parse_args()

    choose_action = load_agent(args.agent)
    runs = [(path.name, load_map(path)) for path in sorted((ROOT / "maps").glob("*.json"))]
    if not args.maps_only:
        runs += [(f"seed {s}", spec_from_dict(generate(s))) for s in parse_range(args.seeds)]

    rows = []
    for name, spec in runs:
        result = play(spec, choose_action)
        rows.append({"run": name, **result})
        if not name.startswith("seed"):
            print(f"{name:28} score {result['score']:4}  exit {str(result['exited']):5}  "
                  f"treasure {result['treasure_value']:3}  energy left {result['remaining_energy']:3}  "
                  f"invalid {result['invalid_actions']}")

    seeds = [r for r in rows if r["run"].startswith("seed")]
    for label, group in (("public maps", [r for r in rows if not r["run"].startswith("seed")]),
                         ("generated seeds", seeds)):
        if not group:
            continue
        print(f"\n{label}: {len(group)} runs")
        print(f"  mean score      {statistics.mean(r['score'] for r in group):7.1f}")
        print(f"  exit rate       {sum(r['exited'] for r in group) / len(group):7.1%}")
        print(f"  mean treasure   {statistics.mean(r['treasure_value'] for r in group):7.1f}")
        print(f"  invalid actions {sum(r['invalid_actions'] for r in group):7d}")
    if seeds:
        failed = [r["run"] for r in seeds if not r["exited"]]
        if failed:
            print("  no exit on:     " + ", ".join(failed[:15]) + (" ..." if len(failed) > 15 else ""))

    if args.csv:
        with open(args.csv, "w", newline="", encoding="utf-8") as handle:
            writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
            writer.writeheader()
            writer.writerows(rows)


if __name__ == "__main__":
    main()
