"""WEEK 1 TUESDAY — Tree Planning Foundations (difficulty 2/5). Guide: README.md

Edit only the three TODO functions (you may add small helper functions).

Provided : known_neighbors, reference_bfs_path (fallback so the starter runs)
You write: TODO 1 bfs_path  -> [] if already there, None if unreachable
           TODO 2 should_collect, TODO 3 select_target (single-detour rule)
Score    : 50 + treasure + energy left - 5 x invalid. 1 energy = 1 point, so
           a detour is worth value - extra energy. E ends the run: never cross it.
Grading  : own BFS 20 (partial credit per test), rules 30, safe exits 20,
           score 15, design note 15. Submitting with USE_MY_BFS = False
           (reference BFS only) loses the 20 BFS points.
Targets  : required level 67 / 88 / 78 / 78, optimum 67 / 90 / 78 / 84
           (warmup / two_branches / greedy_trap / energy_budget).
Tests    : tests/test_student_todo.py fails on the starter; that is expected.
"""

from treasure_explorer.model import Action, Observation, TreasureInfo
from policy_helpers import known_neighbors, reference_bfs_path, safe_known_move

Position = tuple[int, int]
COLLECT_COST = 1

# False: the agent routes with the provided reference_bfs_path.
# True:  the agent routes with YOUR bfs_path (set this once TODO 1 passes).
# Submitting with False (reference BFS only) costs 20 points. See README 7.
USE_MY_BFS = False


def make_state() -> dict:
    """Persistent values for one map run. The fixed agent.py resets this per map."""
    return {"target": None}


# ======================== STUDENT TODO 1 ========================
def bfs_path(
    obs: Observation,
    start: Position,
    goal: Position | None,
    forbidden: tuple[Position, ...] = (),
) -> list[Action] | None:
    """Shortest list of MOVE actions from ``start`` to ``goal``.

    Contract (checked by tests/test_student_todo.py):
    - ``start == goal``            -> ``[]``   (already there, zero moves)
    - goal unreachable or ``None`` -> ``None`` (NOT [], so the two cases differ)
    - otherwise the list of actions of a minimum-step route
    - never enter a cell in ``forbidden`` (except that ``goal`` itself is never
      forbidden by the caller); walls and ``?`` are never entered

    Implement BFS with a queue and a ``parent`` dictionary, then walk the
    parents back from ``goal`` to rebuild the route. Use
    ``known_neighbors(obs, cell, forbidden)`` to list the neighbours.
    Calling ``reference_bfs_path`` here earns no credit: the tests disable it.
    """
    raise NotImplementedError("TODO 1: implement BFS with parent-based path recovery")


def find_path(
    obs: Observation,
    start: Position,
    goal: Position | None,
    forbidden: tuple[Position, ...] = (),
) -> list[Action] | None:
    """Provided: your bfs_path if USE_MY_BFS is True, else the reference BFS."""
    search = bfs_path if USE_MY_BFS else reference_bfs_path
    return search(obs, start, goal, forbidden)


def route_length(obs: Observation, start: Position, goal: Position | None) -> int | None:
    """Provided: number of moves start -> goal that never passes through E.

    Entering E ends the run immediately, so a route to anything other than E
    must treat E as a wall.
    """
    forbidden = () if goal == obs.exit_position else (obs.exit_position,)
    route = find_path(obs, start, goal, forbidden)
    return None if route is None else len(route)


# ======================== STUDENT TODO 2 ========================
def should_collect(obs: Observation, treasure: TreasureInfo, state: dict) -> bool:
    """Called when standing on an uncollected treasure. Return True to COLLECT.

    Collecting costs 1 energy, and every unit of energy left at the exit is one
    point, so collecting gains ``value - 1`` points. It is only allowed if the
    energy left after collecting still covers the route to the exit.
    """
    return False  # starter: never collects


# ======================== STUDENT TODO 3 ========================
def select_target(obs: Observation, state: dict) -> Position | None:
    """Return the next destination: one uncollected treasure, or the exit.

    Single-detour rule (the required level this week). For each treasure t:
        total  = d(here, t) + 1 (COLLECT) + d(t, E)
        extra  = total - d(here, E)          # energy spent because of t
        gain   = t.value - extra             # net points for visiting t
    Choose the treasure with the largest positive gain whose ``total`` fits in
    ``obs.energy``; if none, return ``obs.exit_position``.
    ``d`` is ``route_length`` above. It returns None for unreachable cells.

    Bonus (not required, previews Thursday): two public maps score higher if
    you also consider the ORDER of several treasures. See README.
    """
    return obs.exit_position  # starter: walk straight to the exit


# ===================== PROVIDED ORCHESTRATION ===================
def choose_movement(obs: Observation, state: dict) -> Action:
    """Re-plans every turn: pick a target, then take the first BFS step to it."""
    state["target"] = select_target(obs, state)
    target = state["target"]
    forbidden = () if target == obs.exit_position else (obs.exit_position,)
    route = find_path(obs, obs.position, target, forbidden)
    return route[0] if route else safe_known_move(obs)
