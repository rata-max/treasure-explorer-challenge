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
    def test_collect_turn_preserves_the_same_state_object(self):
        agent = load_fixed_agent()
        state_ids = []

        def collect(_obs, _treasure, state):
            state["marker"] = "kept"
            state_ids.append(id(state))
            return True

        def move(_obs, state):
            self.assertEqual("kept", state["marker"])
            state_ids.append(id(state))
            return Action.MOVE_LEFT

        agent.should_collect = collect
        agent.choose_movement = move
        grid = ("STE",)
        before = Observation(0, (0, 1), (0, 2), 10, grid, (TreasureInfo((0, 1), 5, False),))
        after = Observation(1, (0, 1), (0, 2), 9, grid, (TreasureInfo((0, 1), 5, True),))

        self.assertEqual(Action.COLLECT, agent.choose_action(before))
        self.assertEqual(Action.MOVE_LEFT, agent.choose_action(after))
        self.assertEqual(state_ids[0], state_ids[1])

    def test_new_turn_zero_resets_state(self):
        agent = load_fixed_agent()
        seen = []

        def move(_obs, state):
            seen.append(id(state))
            return Action.MOVE_RIGHT

        agent.choose_movement = move
        empty = Observation(0, (0, 0), (0, 2), 10, ("S.E",), ())
        agent.choose_action(empty)
        agent.choose_action(empty)
        self.assertNotEqual(seen[0], seen[1])


if __name__ == "__main__":
    unittest.main()
