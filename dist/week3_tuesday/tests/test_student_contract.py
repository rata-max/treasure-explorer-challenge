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
        state_objects = []

        def collect(_obs, _treasure, _exit_cost, state):
            state["marker"] = "kept"
            state_objects.append(state)
            return True

        def move(_obs):
            self.assertEqual("kept", agent._POLICY_STATE["marker"])
            state_objects.append(agent._POLICY_STATE)
            return Action.MOVE_LEFT

        agent.should_collect = collect
        agent._choose_movement = move
        grid = ("STE",)
        before = Observation(
            0, (0, 1), (0, 2), 10, grid, (TreasureInfo((0, 1), 5, False),)
        )
        after = Observation(
            1, (0, 1), (0, 2), 9, grid, (TreasureInfo((0, 1), 5, True),)
        )

        self.assertEqual(Action.COLLECT, agent.choose_action(before))
        self.assertEqual(Action.MOVE_LEFT, agent.choose_action(after))
        self.assertIs(state_objects[0], state_objects[1])

    def test_new_turn_zero_creates_independent_policy_state(self):
        agent = load_fixed_agent()
        empty = Observation(0, (0, 0), (0, 2), 10, ("S.E",), ())

        agent.choose_action(empty)
        first_state = agent._POLICY_STATE
        agent.choose_action(empty)
        second_state = agent._POLICY_STATE

        self.assertIsNot(first_state, second_state)

    def test_hidden_exit_does_not_call_student_exploration_rule(self):
        agent = load_fixed_agent()
        calls = []

        def continue_rule(*args):
            calls.append(args)
            return False

        agent.should_continue_exploring = continue_rule
        fog = Observation(0, (0, 0), None, 10, ("S.?",), ())
        self.assertEqual(Action.MOVE_RIGHT, agent.choose_action(fog))
        self.assertEqual([], calls)


if __name__ == "__main__":
    unittest.main()
