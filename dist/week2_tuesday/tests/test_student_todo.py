"""Behaviour tests for YOUR TODOs. They fail on the starter; make them pass."""

import unittest
from pathlib import Path

from treasure_explorer.model import Action, Observation, TreasureInfo
from treasure_explorer.runner import run

import student_policy as sp

ROOT = Path(__file__).resolve().parents[1]
# Score of the required single-detour rule with correct Dijkstra costs.
REQUIRED = {"cycle_detour.json": 100, "energy_illusion.json": 87, "exit_in_the_way.json": 92,
            "mud_shortcut.json": 154, "terrain_choice.json": 91, "water_crossing.json": 99,
            "weighted_maze.json": 106}

# Top row: 4 moves but 4 + 4 + 1 + 1 = 10 energy. Bottom detour: 6 moves, 6 energy.
MUD = ("SMM.E",
       ".....")


def obs_for(grid, position, energy=100, treasures=()):
    exit_pos = next(((r, c) for r, row in enumerate(grid) for c, t in enumerate(row) if t == "E"), None)
    return Observation(0, position, exit_pos, energy, tuple(grid), tuple(treasures))


def walk(start, actions):
    delta = {Action.MOVE_UP: (-1, 0), Action.MOVE_DOWN: (1, 0),
             Action.MOVE_LEFT: (0, -1), Action.MOVE_RIGHT: (0, 1)}
    cells = [start]
    for a in actions:
        dr, dc = delta[a]
        cells.append((cells[-1][0] + dr, cells[-1][1] + dc))
    return cells


def energy_of(grid, cells):
    cost = {".": 1, "S": 1, "E": 1, "T": 1, "M": 4, "W": 7}
    return sum(cost[grid[r][c]] for r, c in cells[1:])


class DijkstraTests(unittest.TestCase):
    def test_same_cell(self):
        self.assertEqual(([], 0), sp.dijkstra_path(obs_for(MUD, (0, 0)), (0, 0), (0, 0)))

    def test_unreachable(self):
        grid = ("S#E",)
        self.assertEqual((None, None), sp.dijkstra_path(obs_for(grid, (0, 0)), (0, 0), (0, 2)))
        self.assertEqual((None, None), sp.dijkstra_path(obs_for(grid, (0, 0)), (0, 0), None))

    def test_cheaper_detour_beats_fewer_steps(self):
        route, cost = sp.dijkstra_path(obs_for(MUD, (0, 0)), (0, 0), (0, 4))
        self.assertEqual(6, cost)
        cells = walk((0, 0), route)
        self.assertEqual((0, 4), cells[-1])
        self.assertEqual(6, energy_of(MUD, cells), "returned cost must match the route")

    def test_forbidden_and_unknown_cells(self):
        o = obs_for(MUD, (0, 0))
        route, cost = sp.dijkstra_path(o, (0, 0), (0, 4), forbidden=((1, 2),))
        self.assertEqual(10, cost)
        self.assertNotIn((1, 2), walk((0, 0), route))
        fog = obs_for(("S?E",), (0, 0))
        self.assertEqual((None, None), sp.dijkstra_path(fog, (0, 0), (0, 2)))

    def test_water_versus_long_way(self):
        # water costs 7: straight = 7 + 1 = 8, around = 8 moves of cost 1 -> tie broken by cost only
        grid = ("SWE",
                "#.#",
                "#.#",
                "#.#",
                "...")
        _, cost = sp.dijkstra_path(obs_for(grid, (0, 0)), (0, 0), (0, 2))
        self.assertEqual(8, cost)


class DecisionTests(unittest.TestCase):
    GRID = ("#######",
            "#S...E#",
            "###M###",
            "###T###",
            "#######")

    def test_mud_detour_priced_by_energy(self):
        # d(S,T) = 2 + 4 + 1 = 7, d(T,E) = 4 + 1 + 2 = 7, direct = 4
        # -> extra = 7 + 1 + 7 - 4 = 11
        t = TreasureInfo((3, 3), 11, False)
        o = obs_for(self.GRID, (1, 1), energy=50, treasures=(t,))
        self.assertEqual((1, 5), sp.select_target(o, sp.make_state()), "gain 0 is not worth it")
        t = TreasureInfo((3, 3), 12, False)
        o = obs_for(self.GRID, (1, 1), energy=50, treasures=(t,))
        self.assertEqual((3, 3), sp.select_target(o, sp.make_state()))

    def test_budget_uses_energy_not_steps(self):
        t = TreasureInfo((3, 3), 40, False)
        o = obs_for(self.GRID, (1, 1), energy=14, treasures=(t,))  # needs 7 + 1 + 7 = 15
        self.assertEqual((1, 5), sp.select_target(o, sp.make_state()))
        o = obs_for(self.GRID, (1, 1), energy=15, treasures=(t,))
        self.assertEqual((3, 3), sp.select_target(o, sp.make_state()))

    def test_collect_keeps_exit_energy(self):
        t = TreasureInfo((3, 3), 40, False)
        o = obs_for(self.GRID, (3, 3), energy=7, treasures=(t,))  # exit costs 7
        self.assertFalse(sp.should_collect(o, t, sp.make_state()))
        o = obs_for(self.GRID, (3, 3), energy=8, treasures=(t,))
        self.assertTrue(sp.should_collect(o, t, sp.make_state()))

    def test_route_cost_never_crosses_exit(self):
        grid = ("S.E.T",)
        o = obs_for(grid, (0, 0))
        self.assertIsNone(sp.route_cost(o, (0, 0), (0, 4)))


class FullRunTests(unittest.TestCase):
    def test_every_map_meets_the_required_level(self):
        for path in sorted((ROOT / "maps").glob("*.json")):
            result, _ = run(path, ROOT / "agent.py")
            self.assertTrue(result["exited"], path.name)
            self.assertEqual(0, result["invalid_actions"], path.name)
            self.assertGreaterEqual(result["score"], REQUIRED[path.name], path.name)


if __name__ == "__main__":
    unittest.main()
