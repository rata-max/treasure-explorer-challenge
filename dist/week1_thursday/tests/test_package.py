import unittest
from pathlib import Path

from treasure_explorer.runner import load_map, run


ROOT = Path(__file__).resolve().parents[1]


class PackageTests(unittest.TestCase):
    def test_all_public_maps_load(self):
        maps = sorted((ROOT / "maps").glob("*.json"))
        self.assertEqual(5, len(maps))
        for path in maps:
            spec = load_map(path)
            self.assertEqual("public", spec.visibility)

    def test_safe_starter_exits_every_map(self):
        for path in sorted((ROOT / "maps").glob("*.json")):
            result, _ = run(path, ROOT / "agent.py")
            self.assertTrue(result["exited"], path.name)
            self.assertEqual(0, result["invalid_actions"], path.name)


if __name__ == "__main__":
    unittest.main()
