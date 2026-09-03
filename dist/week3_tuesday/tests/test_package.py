import unittest
from pathlib import Path

from treasure_explorer.engine import Game
from treasure_explorer.model import Action
from treasure_explorer.runner import load_map, run

ROOT = Path(__file__).resolve().parents[1]


class PackageTests(unittest.TestCase):
    def test_only_the_public_practice_map_is_distributed(self):
        maps = sorted((ROOT / "maps").glob("*.json"))
        self.assertEqual(["robustness_practice.json"], [path.name for path in maps])
        self.assertEqual("local", load_map(maps[0]).visibility)

    def test_safe_starter_exits_public_map_without_invalid_actions(self):
        path = ROOT / "maps" / "robustness_practice.json"
        result, _ = run(path, ROOT / "agent.py")
        self.assertTrue(result["exited"])
        self.assertEqual(0, result["invalid_actions"])

    def test_public_ground_truth_is_masked_in_agent_observation(self):
        path = ROOT / "maps" / "robustness_practice.json"
        game = Game(load_map(path))

        initial = game.observation()
        self.assertTrue(any("?" in row for row in initial.grid))
        self.assertIsNone(initial.exit_position)

        # The treasure at (3, 1) becomes visible from (2, 1), but its value is
        # still hidden from the agent until it actually reaches the T cell.
        game.step(Action.MOVE_DOWN)
        nearby = next(t for t in game.observation().treasures if t.position == (3, 1))
        self.assertIsNone(nearby.value)

        game.step(Action.MOVE_DOWN)
        reached = next(t for t in game.observation().treasures if t.position == (3, 1))
        self.assertEqual(14, reached.value)


if __name__ == "__main__":
    unittest.main()
