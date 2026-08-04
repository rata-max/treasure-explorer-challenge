import unittest
from collections import deque

from treasure_explorer.engine import Game
from treasure_explorer.model import Action
from treasure_explorer.runner import load_map


class EngineTests(unittest.TestCase):
    def test_week1_maps_are_connected_trees(self):
        for name in ("easy", "medium", "hard"):
            grid = load_map(f"maps/week1_tree_{name}.json").grid
            vertices = {(r, c) for r, row in enumerate(grid) for c, tile in enumerate(row) if tile != "#"}
            edges = sum(
                (r + dr, c + dc) in vertices
                for r, c in vertices
                for dr, dc in ((1, 0), (0, 1))
            )
            queue = deque([next(iter(vertices))])
            seen = {queue[0]}
            while queue:
                r, c = queue.popleft()
                for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nxt = (r + dr, c + dc)
                    if nxt in vertices and nxt not in seen:
                        seen.add(nxt)
                        queue.append(nxt)
            self.assertEqual(len(seen), len(vertices), name)
            self.assertEqual(edges, len(vertices) - 1, name)

    def test_key_is_required_before_exit(self):
        game = Game(load_map("maps/week1_tree_easy.json"))
        for _ in range(9):
            game.step(Action.MOVE_RIGHT)
        self.assertFalse(game.exited)

    def test_key_unlocks_exit(self):
        game = Game(load_map("maps/week1_tree_easy.json"))
        game.step(Action.MOVE_RIGHT)
        game.step(Action.MOVE_RIGHT)
        game.step(Action.MOVE_DOWN)
        game.step(Action.MOVE_DOWN)
        self.assertTrue(game.has_key)
        game.step(Action.MOVE_UP)
        game.step(Action.MOVE_UP)
        for _ in range(7):
            game.step(Action.MOVE_RIGHT)
        self.assertTrue(game.exited)

    def test_battery_restores_energy(self):
        game = Game(load_map("maps/week1_tree_easy.json"))
        for _ in range(8):
            game.step(Action.MOVE_RIGHT)
        before = game.energy
        game.step(Action.MOVE_DOWN)
        game.step(Action.MOVE_DOWN)
        self.assertGreater(game.energy, before)

    def test_hidden_terrain_is_revealed_when_adjacent(self):
        game = Game(load_map("maps/example_medium.json"))
        self.assertEqual(game.observation().grid[1][4], "?")
        game.step(Action.MOVE_RIGHT)
        game.step(Action.MOVE_RIGHT)
        self.assertEqual(game.observation().grid[1][4], "M")

    def test_treasure_value_is_revealed_on_arrival(self):
        game = Game(load_map("maps/example_easy.json"))
        for _ in range(3):
            game.step(Action.MOVE_RIGHT)
        self.assertEqual(game.observation().treasures[0].value, 12)

    def test_exit_confirms_score(self):
        game = Game(load_map("maps/example_easy.json"))
        for _ in range(3):
            game.step(Action.MOVE_RIGHT)
        game.step(Action.COLLECT)
        for _ in range(3):
            game.step(Action.MOVE_RIGHT)
        result = game.result()
        self.assertTrue(result["exited"])
        self.assertEqual(result["score"], 12 + 28)

    def test_failure_to_exit_scores_zero(self):
        game = Game(load_map("maps/example_easy.json"))
        game.energy = 0
        self.assertEqual(game.result()["score"], 0)


if __name__ == "__main__":
    unittest.main()
