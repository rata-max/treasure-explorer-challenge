"""Behaviour tests for YOUR TODOs. The starter fails some of them.

These are minimum bars. The final evaluation uses unpublished generator seeds
and ranks policies by mean score, exit rate and invalid actions.
"""

import statistics
import unittest
from pathlib import Path

from treasure_explorer.generator import generate
from treasure_explorer.model import Observation, TreasureInfo
from treasure_explorer.runner import load_agent, run

import student_policy as sp
from evaluate import play, spec_from_dict
from policy_helpers import Option

ROOT = Path(__file__).resolve().parents[1]
GRID = ("S....T....E",)


def on_treasure(energy, value, exit_known=True):
    t = TreasureInfo((0, 5), value, False)
    return Observation(10, (0, 5), (0, 10) if exit_known else None, energy, GRID, (t,)), t


class CollectTests(unittest.TestCase):
    def test_value_one_is_never_worth_it(self):
        obs, t = on_treasure(100, 1)
        self.assertFalse(sp.should_collect(obs, t, 5, {"observed_values": [1]}))

    def test_known_exit_boundary(self):
        margin = sp.SAFETY_MARGIN
        obs, t = on_treasure(1 + 5 + margin, 30)
        self.assertTrue(sp.should_collect(obs, t, 5, {"observed_values": [30]}))
        obs, t = on_treasure(5 + margin, 30)
        self.assertFalse(sp.should_collect(obs, t, 5, {"observed_values": [30]}))

    def test_low_value_is_still_profitable(self):
        # Worse than every earlier treasure, but COLLECT only costs 1 energy.
        obs, t = on_treasure(100, 6)
        self.assertTrue(sp.should_collect(obs, t, 5, {"observed_values": [40, 45, 6]}))

    def test_unknown_exit_returns_a_decision(self):
        obs, t = on_treasure(200, 30, exit_known=False)
        self.assertIsInstance(sp.should_collect(obs, t, None, {"observed_values": [30]}), bool)


class TargetTests(unittest.TestCase):
    def test_never_picks_an_option_that_cannot_get_home(self):
        # E known, 20 energy, exit 5 away. The only option needs 12 + 10 = 22.
        obs = Observation(10, (0, 5), (0, 10), 20, GRID, ())
        far = Option("frontier", (0, 0), 12, 10, 8)
        choice = sp.choose_target(obs, (far,), {"observed_values": [40]})
        self.assertIsNone(choice)

    def test_result_is_an_option_or_none(self):
        obs = Observation(10, (0, 5), (0, 10), 80, GRID, ())
        options = (Option("frontier", (0, 0), 5, 10, 6), Option("treasure", (0, 3), 2, 7, 3, None))
        choice = sp.choose_target(obs, options, {"observed_values": [20, 30]})
        self.assertTrue(choice is None or choice in options)


class FullRunTests(unittest.TestCase):
    def test_public_maps_exit_cleanly(self):
        for path in sorted((ROOT / "maps").glob("*.json")):
            result, _ = run(path, ROOT / "agent.py")
            self.assertTrue(result["exited"], path.name)
            self.assertEqual(0, result["invalid_actions"], path.name)

    def test_generated_minimum_bar(self):
        # starter: mean 166.8, exit 90 %. Required: mean >= 200 and exit >= 90 %.
        act = load_agent(ROOT / "agent.py")
        results = [play(spec_from_dict(generate(seed)), act) for seed in range(30)]
        self.assertGreaterEqual(sum(r["exited"] for r in results), 27)
        self.assertEqual(0, sum(r["invalid_actions"] for r in results))
        self.assertGreaterEqual(statistics.mean(r["score"] for r in results), 200)


if __name__ == "__main__":
    unittest.main()
