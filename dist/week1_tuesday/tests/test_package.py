import unittest
from pathlib import Path

from treasure_explorer.runner import load_map


ROOT = Path(__file__).resolve().parents[1]


class PackageTests(unittest.TestCase):
    def test_all_public_maps_load(self):
        maps = sorted((ROOT / "maps").glob("*.json"))
        self.assertEqual(4, len(maps))
        for path in maps:
            spec = load_map(path)
            self.assertEqual("public", spec.visibility)
            self.assertTrue(all(tile in "#.SET" for row in spec.grid for tile in row),
                            f"{path.name}: Week 1 maps use unit-cost tiles only")


if __name__ == "__main__":
    unittest.main()
