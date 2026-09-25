import unittest
from pathlib import Path

from treasure_explorer.engine import Game
from treasure_explorer.generator import generate
from treasure_explorer.model import Action
from treasure_explorer.runner import load_map

ROOT = Path(__file__).resolve().parents[1]
PUBLIC = ["costly_terrain.json", "decoys.json", "early_exit.json", "low_budget.json",
          "robustness_practice.json"]


class PackageTests(unittest.TestCase):
    def test_public_maps(self):
        maps = sorted(p.name for p in (ROOT / "maps").glob("*.json"))
        self.assertEqual(PUBLIC, maps)
        for name in maps:
            spec = load_map(ROOT / "maps" / name)
            self.assertEqual("local", spec.visibility)
            self.assertTrue(spec.hidden_values)

    def test_public_ground_truth_is_masked_in_agent_observation(self):
        game = Game(load_map(ROOT / "maps" / "robustness_practice.json"))
        initial = game.observation()
        self.assertTrue(any("?" in row for row in initial.grid))
        self.assertIsNone(initial.exit_position)
        # (3, 1) becomes visible from (2, 1) but its value stays hidden until reached.
        game.step(Action.MOVE_DOWN)
        nearby = next(t for t in game.observation().treasures if t.position == (3, 1))
        self.assertIsNone(nearby.value)
        game.step(Action.MOVE_DOWN)
        reached = next(t for t in game.observation().treasures if t.position == (3, 1))
        self.assertEqual(14, reached.value)

    def test_generator_is_deterministic_and_valid(self):
        import json, tempfile, os
        for seed in (0, 1, 2, 3, 99):
            self.assertEqual(generate(seed), generate(seed))
            with tempfile.TemporaryDirectory() as tmp:
                path = os.path.join(tmp, "m.json")
                with open(path, "w", encoding="utf-8") as handle:
                    json.dump(generate(seed), handle)
                spec = load_map(path)  # validates tiles and T/treasure agreement
                self.assertEqual("local", spec.visibility)


if __name__ == "__main__":
    unittest.main()
