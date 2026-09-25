"""Behaviour tests for YOUR TODOs. They fail on the starter; make them pass.

BfsTests grade YOUR bfs_path (20 points, partial credit per test, see README).
test_submission_uses_my_bfs fails while USE_MY_BFS is False (-20 points).
The provided reference_bfs_path is disabled while they run, so a bfs_path that
only calls the reference fails them. The other tests use whichever BFS the
USE_MY_BFS switch selects.
"""

import unittest
from pathlib import Path

from treasure_explorer.model import Action, Observation, TreasureInfo
from treasure_explorer.runner import run

import policy_helpers as ph
import student_policy as sp

ROOT = Path(__file__).resolve().parents[1]
DIRECT_EXIT_SCORES = {"warmup.json": 60, "two_branches.json": 76,
                  "greedy_trap.json": 63, "energy_budget.json": 66}


def obs_for(grid, position, energy=100, treasures=()):
    exit_pos = next((r, c) for r, row in enumerate(grid) for c, t in enumerate(row) if t == "E")
    return Observation(0, position, exit_pos, energy, tuple(grid), tuple(treasures))


def walk(start, actions):
    delta = {Action.MOVE_UP: (-1, 0), Action.MOVE_DOWN: (1, 0),
             Action.MOVE_LEFT: (0, -1), Action.MOVE_RIGHT: (0, 1)}
    cells = [start]
    for a in actions:
        r, c = cells[-1]
        dr, dc = delta[a]
        cells.append((r + dr, c + dc))
    return cells


def _reference_disabled(*_args, **_kwargs):
    raise AssertionError("bfs_path must be your own BFS, not a call to reference_bfs_path")


class BfsTests(unittest.TestCase):
    """YOUR bfs_path. README 7: contract 4, shortest 8, forbidden 4, unknown 4."""

    GRID = ("#######",
            "#S...E#",
            "#.###.#",
            "#.....#",
            "#######")

    def setUp(self):
        self._saved = (ph.reference_bfs_path, sp.__dict__.get("reference_bfs_path"))
        ph.reference_bfs_path = _reference_disabled
        if "reference_bfs_path" in sp.__dict__:
            sp.reference_bfs_path = _reference_disabled

    def tearDown(self):
        ph.reference_bfs_path = self._saved[0]
        if self._saved[1] is not None:
            sp.reference_bfs_path = self._saved[1]

    def test_contract_same_cell_is_empty_route(self):
        o = obs_for(self.GRID, (1, 1))
        self.assertEqual([], sp.bfs_path(o, (1, 1), (1, 1)))

    def test_contract_unreachable_is_none(self):
        grid = ("#####", "#S#E#", "#####")
        o = obs_for(grid, (1, 1))
        self.assertIsNone(sp.bfs_path(o, (1, 1), (1, 3)))
        self.assertIsNone(sp.bfs_path(o, (1, 1), None))

    def test_shortest_route_is_valid_and_minimal(self):
        o = obs_for(self.GRID, (1, 1))
        route = sp.bfs_path(o, (1, 1), (3, 5))
        self.assertEqual(6, len(route))
        cells = walk((1, 1), route)
        self.assertEqual((3, 5), cells[-1])
        for r, c in cells:
            self.assertNotEqual("#", self.GRID[r][c])

    def test_forbidden_cell_is_avoided(self):
        o = obs_for(self.GRID, (1, 1))
        route = sp.bfs_path(o, (1, 1), (1, 4), forbidden=((1, 3),))
        self.assertNotIn((1, 3), walk((1, 1), route))
        self.assertEqual(9, len(route))

    def test_unknown_cells_are_not_walkable(self):
        grid = ("#####", "#S?E#", "#####")
        o = obs_for(grid, (1, 1))
        self.assertIsNone(sp.bfs_path(o, (1, 1), (1, 3)))


class SubmissionTests(unittest.TestCase):
    def test_submission_uses_my_bfs(self):
        self.assertTrue(
            sp.USE_MY_BFS,
            "USE_MY_BFS is False: the agent runs on reference_bfs_path only (-20 points, README 7)",
        )


class DecisionTests(unittest.TestCase):
    def test_collect_needs_profit(self):
        grid = ("#####", "#STE#", "#####")
        here = TreasureInfo((1, 2), 1, False)
        o = obs_for(grid, (1, 2), energy=10, treasures=(here,))
        self.assertFalse(sp.should_collect(o, here, sp.make_state()))

    def test_collect_needs_exit_energy(self):
        grid = ("#######", "#ST..E#", "#######")
        here = TreasureInfo((1, 2), 9, False)
        # 3 moves to E remain; after COLLECT we would have 2 < 3.
        o = obs_for(grid, (1, 2), energy=3, treasures=(here,))
        self.assertFalse(sp.should_collect(o, here, sp.make_state()))
        o = obs_for(grid, (1, 2), energy=4, treasures=(here,))
        self.assertTrue(sp.should_collect(o, here, sp.make_state()))

    def test_target_skips_unprofitable_detour(self):
        # Branch treasure: 3 down + 3 back up + COLLECT 1 = 7 extra energy.
        # value 7 -> gain 0 (not worth it); value 8 -> gain 1 (worth it).
        grid = ("#######", "#S...E#", "###.###", "###.###", "###T###", "#######")
        t = TreasureInfo((4, 3), 7, False)
        o = obs_for(grid, (1, 1), energy=50, treasures=(t,))
        self.assertEqual((1, 5), sp.select_target(o, sp.make_state()))
        t = TreasureInfo((4, 3), 8, False)
        o = obs_for(grid, (1, 1), energy=50, treasures=(t,))
        self.assertEqual((4, 3), sp.select_target(o, sp.make_state()))

    def test_target_respects_budget(self):
        grid = ("#######", "#S...E#", "###.###", "###.###", "###T###", "#######")
        t = TreasureInfo((4, 3), 30, False)
        # direct = 4 moves; via treasure = 5 (S->T) + 1 (COLLECT) + 5 (T->E) = 11
        o = obs_for(grid, (1, 1), energy=10, treasures=(t,))
        self.assertEqual((1, 5), sp.select_target(o, sp.make_state()))
        o = obs_for(grid, (1, 1), energy=11, treasures=(t,))
        self.assertEqual((4, 3), sp.select_target(o, sp.make_state()))

    def test_collected_treasure_is_ignored(self):
        grid = ("#######", "#S...E#", "###.###", "###T###", "#######")
        t = TreasureInfo((3, 3), 30, True)
        o = obs_for(grid, (1, 1), energy=50, treasures=(t,))
        self.assertEqual((1, 5), sp.select_target(o, sp.make_state()))


class FullRunTests(unittest.TestCase):
    def test_every_map_exits_cleanly_and_beats_going_straight_out(self):
        for path in sorted((ROOT / "maps").glob("*.json")):
            result, _ = run(path, ROOT / "agent.py")
            self.assertTrue(result["exited"], path.name)
            self.assertEqual(0, result["invalid_actions"], path.name)
            self.assertGreater(result["score"], DIRECT_EXIT_SCORES[path.name], path.name)


if __name__ == "__main__":
    unittest.main()
