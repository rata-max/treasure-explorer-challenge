"""WEEK 2 TUESDAY — Weighted Graph Routes (difficulty 3/5). Guide: README.md

Edit only the TODO functions (small helper functions are fine).

Provided : known_neighbors (with entry cost), bfs_path FOR COMPARISON ONLY
You write: TODO 1 dijkstra_path -> ([], 0) if there, (None, None) if unreachable
           TODO 2 should_collect, TODO 3 select_target with ENERGY costs
Terrain  : entering . S E T = 1, mud M = 4, water W = 7; COLLECT = 1.
Watch out: hop-count BFS scores 0 on energy_illusion.json; route_cost and the
           orchestration keep routes off E (exit_in_the_way.json).
Required : the single-detour score on all 7 maps (see README section 4).
Grading  : Dijkstra 30, rules 20, required scores 20, BFS vs Dijkstra table
           15, design note 15.
Tests    : tests/test_student_todo.py fails on the starter; make it pass.
"""

from treasure_explorer.model import Action, Observation, TreasureInfo
from policy_helpers import known_neighbors, safe_known_move

Position = tuple[int, int]
COLLECT_COST = 1


def make_state() -> dict:
    return {"target": None}


# ======================== STUDENT TODO 1 ========================
def dijkstra_path(
    obs: Observation,
    start: Position,
    goal: Position | None,
    forbidden: tuple[Position, ...] = (),
) -> tuple[list[Action] | None, int | None]:
    """Minimum-ENERGY route and its cost.

    Contract (checked by tests/test_student_todo.py):
    - ``start == goal``            -> ``([], 0)``
    - goal unreachable or ``None`` -> ``(None, None)``
    - otherwise ``(actions, cost)`` where cost = sum of the entry costs of the
      cells entered (``known_neighbors`` yields that cost as its 3rd item)
    - never enter a cell in ``forbidden``, a wall, or ``?``

    Use ``heapq`` as the priority queue and a ``parent`` dictionary for the
    route. A cell may be pushed several times; skip a popped entry whose cost
    is larger than the best cost already recorded for that cell (stale entry).
    Required complexity: O((V + E) log V). Do NOT use BFS: step count is not
    energy when mud (4) or water (7) is on the map.
    """
    raise NotImplementedError("TODO 1: implement Dijkstra with a heap and parents")


def route_cost(obs: Observation, start: Position, goal: Position | None) -> int | None:
    """Provided: energy of the cheapest route that never passes through E."""
    forbidden = () if goal == obs.exit_position else (obs.exit_position,)
    return dijkstra_path(obs, start, goal, forbidden)[1]


# ======================== STUDENT TODO 2 ========================
def should_collect(obs: Observation, treasure: TreasureInfo, state: dict) -> bool:
    """Collect when value > 1 and the energy left after COLLECT still covers
    ``route_cost(here, E)``."""
    return False  # starter: never collects


# ======================== STUDENT TODO 3 ========================
def select_target(obs: Observation, state: dict) -> Position | None:
    """Same single-detour rule as Week 1 Tuesday, but with ENERGY costs:
        extra = c(here, t) + 1 + c(t, E) - c(here, E),  gain = value - extra
    Pick the largest positive gain whose total fits in ``obs.energy``,
    otherwise the exit. ``c`` is ``route_cost`` above (None = unreachable).
    The orchestration calls this again every time a target is reached.
    """
    return obs.exit_position  # starter: walk straight to the exit


# ===================== PROVIDED ORCHESTRATION ===================
def choose_movement(obs: Observation, state: dict) -> Action:
    if state["target"] is None or state["target"] == obs.position:
        state["target"] = select_target(obs, state)
    target = state["target"]
    forbidden = () if target == obs.exit_position else (obs.exit_position,)
    route, _ = dijkstra_path(obs, obs.position, target, forbidden)
    return route[0] if route else safe_known_move(obs)
