import unittest
from pathlib import Path

from treasure_explorer.runner import load_map


ROOT = Path(__file__).resolve().parents[1]


class PackageTests(unittest.TestCase):
    def test_all_public_maps_load(self):
        maps = sorted((ROOT / "maps").glob("*.json"))
        self.assertEqual(7, len(maps))
        for path in maps:
            self.assertEqual("public", load_map(path).visibility)


if __name__ == "__main__":
    unittest.main()
