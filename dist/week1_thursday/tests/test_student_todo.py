"""Behaviour tests for YOUR plan_targets. They fail on the starter."""

import json
import time
import unittest
from pathlib import Path

from treasure_explorer.model import Observation, TreasureInfo
from treasure_explorer.runner import load_map, run
from treasure_explorer.engine import Game

import student_policy as sp

ROOT = Path(__file__).resolve().parents[1]
# Exact optimum of every released map (independently computed).
OPTIMAL = {"budget_cut.json": 118, "challenge.json": 142, "large_tree.json": 136,
           "many_treasures.json": 292, "nearest_trap.json": 146, "shared_branch.json": 89,
           "subset_order.json": 112, "value_trap.json": 101}
TIME_LIMIT = 2.0

# Shared stem: each treasure ALONE costs 11 extra energy (> value 8),
# but both together cost 14 extra (< 16). Only a global plan takes them.
STEM = ("#########",
        "#S.....E#",
        "####.####",
        "####.####",
        "####.####",
        "###T.T###",
        "#########")


def stem_obs(energy):
    ts = (TreasureInfo((5, 3), 8, False), TreasureInfo((5, 5), 8, False))
    return Observation(0, (1, 1), (1, 7), energy, STEM, ts)


class PlanTests(unittest.TestCase):
    def test_plan_ends_at_exit(self):
        plan = sp.plan_targets(stem_obs(50), sp.make_state())
        self.assertEqual((1, 7), plan[-1])

    def test_shared_branch_is_taken_as_a_pair(self):
        plan = sp.plan_targets(stem_obs(50), sp.make_state())
        self.assertEqual({(5, 3), (5, 5)}, set(plan[:-1]))

    def test_pair_dropped_when_budget_is_one_short(self):
        # both treasures need exactly 20 energy
        self.assertEqual([(1, 7)], sp.plan_targets(stem_obs(19), sp.make_state()))
        self.assertEqual(3, len(sp.plan_targets(stem_obs(20), sp.make_state())))


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
