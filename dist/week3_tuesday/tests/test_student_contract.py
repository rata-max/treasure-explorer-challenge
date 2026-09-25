"""Contract of the fixed agent.py (these pass on the starter)."""

from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path

from treasure_explorer.model import Action, Observation, TreasureInfo


def load_fixed_agent():
    path = Path(__file__).parents[1] / "agent.py"
    spec = importlib.util.spec_from_file_location("contract_agent", path)
    module = importlib.util.module_from_spec(spec)
    assert spec and spec.loader
    spec.loader.exec_module(module)
    return module


class StudentContractTests(unittest.TestCase):
    def test_collect_turn_preserves_the_same_policy_state_object(self):
        agent = load_fixed_agent()
        seen = []

        def collect(_obs, _treasure, _exit_cost, state):
            state["marker"] = "kept"
            seen.append(state)
            return True

        def target(_obs, _options, state):
            self.assertEqual("kept", state["marker"])
            seen.append(state)
            return None

        agent.should_collect, agent.choose_target = collect, target
        grid = ("STE",)
        before = Observation(0, (0, 1), (0, 2), 10, grid, (TreasureInfo((0, 1), 5, False),))
        after = Observation(1, (0, 1), (0, 2), 9, grid, (TreasureInfo((0, 1), 5, True),))
        self.assertEqual(Action.COLLECT, agent.choose_action(before))
        self.assertEqual(Action.MOVE_RIGHT, agent.choose_action(after))
        self.assertIs(seen[0], seen[1])
        self.assertEqual([5], seen[0]["observed_values"])

    def test_new_turn_zero_creates_independent_policy_state(self):
        agent = load_fixed_agent()
        empty = Observation(0, (0, 0), (0, 2), 10, ("S.E",), ())
        agent.choose_action(empty)
        first = agent._POLICY_STATE
        agent.choose_action(empty)
        self.assertIsNot(first, agent._POLICY_STATE)

    def test_exit_unknown_none_falls_back_to_cheapest_frontier(self):
        agent = load_fixed_agent()
        agent.choose_target = lambda obs, options, state: None
        fog = Observation(0, (0, 0), None, 10, ("S.?",), ())
        self.assertEqual(Action.MOVE_RIGHT, agent.choose_action(fog))

    def test_options_describe_frontiers_and_hidden_treasures(self):
        agent = load_fixed_agent()
        grid = ("S.T?",
                "..E.")
        obs = Observation(0, (0, 0), (1, 2), 20, grid, (TreasureInfo((0, 2), None, False),))
        agent._new_run_state()
        options = agent.build_options(obs)
        kinds = {(o.kind, o.position) for o in options}
        self.assertIn(("treasure", (0, 2)), kinds)
        self.assertIn(("frontier", (0, 2)), kinds)   # T itself borders "?"
        treasure = next(o for o in options if o.kind == "treasure")
        self.assertEqual(2, treasure.cost_to)
        self.assertEqual(1, treasure.cost_to_exit)    # one step down into E
        self.assertIsNone(treasure.value)

    def test_foreign_option_is_rejected(self):
        agent = load_fixed_agent()
        from policy_helpers import Option
        agent.choose_target = lambda obs, options, state: Option("frontier", (9, 9), 1, 1, 0)
        fog = Observation(0, (0, 0), None, 10, ("S.?",), ())
        with self.assertRaises(ValueError):
            agent.choose_action(fog)

    def test_never_steps_into_unaffordable_terrain(self):
        agent = load_fixed_agent()
        agent.choose_target = lambda obs, options, state: options[0] if options else None
        # Only way forward is water (7) but just 3 energy remain; the fallback must
        # pick an affordable move instead of repeating an invalid one.
        grid = ("S.W?",)
        obs = Observation(5, (0, 1), None, 3, grid, ())
        self.assertEqual(Action.MOVE_LEFT, agent.choose_action(obs))


if __name__ == "__main__":
    unittest.main()
