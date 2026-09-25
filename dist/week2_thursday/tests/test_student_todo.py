"""Behaviour tests for YOUR plan_targets. They fail on the starter."""

import time
import unittest
from pathlib import Path

from treasure_explorer.engine import Game
from treasure_explorer.model import Observation, TreasureInfo
from treasure_explorer.runner import load_map, run

import student_policy as sp
from policy_helpers import route_cost

ROOT = Path(__file__).resolve().parents[1]
# Exact optimum of every released map (independently computed).
OPTIMAL = {"budget_tradeoff.json": 174, "cyclic_order.json": 199, "grand_tour.json": 398,
           "graph_challenge.json": 225, "low_value_bait.json": 226, "pair_or_prize.json": 163,
           "terrain_bundle.json": 171, "tight_budget.json": 141}
TIME_LIMIT = 5.0

# A loop with mud on the top side. Treasures of value 10, 30 and 9 on the bottom.
#   S . . M M . E
#   . # # # # # .
#   T . . T . . T
LOOP = ("S..MM.E",
        ".#####.",
        "T..T..T")


def loop_obs(energy, values=(10, 30, 9)):
    ts = tuple(TreasureInfo(p, v, False) for p, v in zip(((2, 0), (2, 3), (2, 6)), values))
    return Observation(0, (0, 0), (0, 6), energy, LOOP, ts)


def plan_energy(obs, plan):
    here, total = obs.position, 0
    for stop in plan:
        total += route_cost(obs, here, stop)
        if stop != obs.exit_position:
            total += 1  # COLLECT
        here = stop
    return total


class PlanTests(unittest.TestCase):
    def test_plan_is_feasible_and_ends_at_exit(self):
        for energy in (10, 12, 14, 20):
            o = loop_obs(energy)
            plan = sp.plan_targets(o, sp.make_state())
            self.assertEqual((0, 6), plan[-1])
            self.assertLessEqual(plan_energy(o, plan), energy, f"energy={energy}")

    def test_bottom_sweep_when_affordable(self):
        # Bottom row collects all three for 2+1+3+1+3+1+2 = 13 energy vs 10 direct.
        plan = sp.plan_targets(loop_obs(20), sp.make_state())
        self.assertEqual([(2, 0), (2, 3), (2, 6), (0, 6)], plan)

    def test_budget_forces_a_subset(self):
        # 12 energy: the full sweep (13) no longer fits. Best is to collect the
        # 10 and the 30 and then WALK OVER the 9 without collecting it:
        # 2 + 1 + 3 + 1 + 5 = 12 energy for value 40.
        plan = sp.plan_targets(loop_obs(12), sp.make_state())
        self.assertEqual([(2, 0), (2, 3), (0, 6)], plan)


class FullRunTests(unittest.TestCase):
    def test_every_map_reaches_the_optimum(self):
        for path in sorted((ROOT / "maps").glob("*.json")):
            result, _ = run(path, ROOT / "agent.py")
            self.assertTrue(result["exited"], path.name)
            self.assertEqual(0, result["invalid_actions"], path.name)
            self.assertEqual(OPTIMAL[path.name], result["score"], path.name)

    def test_planning_time_limit(self):
        for path in sorted((ROOT / "maps").glob("*.json")):
            obs = Game(load_map(path)).observation()
            started = time.perf_counter()
            sp.plan_targets(obs, sp.make_state())
            elapsed = time.perf_counter() - started
            self.assertLess(elapsed, TIME_LIMIT, f"{path.name}: {elapsed:.2f}s")


if __name__ == "__main__":
    unittest.main()
