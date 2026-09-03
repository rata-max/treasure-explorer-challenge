"""Fixed online-planning adapter for the integrated Week 3 final.

DO NOT EDIT OR SUBMIT THIS FILE.

The coding activity now finishes in one three-hour Tuesday session; Thursday is
reserved for presentations. This adapter provides the partial-observation
machinery so the lab can focus on policy decisions: persistent state, frontier
generation, Dijkstra routing, online replanning, exit avoidance while exploring,
and COLLECT lifecycle.

Students edit only the two decision rules in ``student_policy.py``.
"""

from __future__ import annotations

from treasure_explorer.model import Action, Observation, TreasureInfo
from policy_helpers import dijkstra_path, known_frontiers, safe_known_move
from student_policy import should_collect, should_continue_exploring


_MOVE_ACTIONS = frozenset(
    {Action.MOVE_UP, Action.MOVE_DOWN, Action.MOVE_LEFT, Action.MOVE_RIGHT}
)
_INFINITY = 10**9
_PLANNER_STATE: dict = {}
_POLICY_STATE: dict = {}
_LAST_TURN: int | None = None


def _new_run_state() -> None:
    """Create independent planning and student-policy memory for one map."""
    global _PLANNER_STATE, _POLICY_STATE
    _PLANNER_STATE = {"visited": set(), "seen_treasure_values": set()}
    _POLICY_STATE = {"observed_values": []}


def _reset_only_for_a_new_run(obs: Observation) -> None:
    """Reset state at a map boundary, never after reaching/collecting treasure."""
    global _LAST_TURN
    if _LAST_TURN is None or obs.turn == 0 or obs.turn <= _LAST_TURN:
        _new_run_state()
    _LAST_TURN = obs.turn


def _uncollected_treasure_here(obs: Observation) -> TreasureInfo | None:
    # The grid character remains "T" after collection. TreasureInfo.collected
    # is the authoritative flag.
    return next(
        (
            treasure
            for treasure in obs.treasures
            if treasure.position == obs.position and not treasure.collected
        ),
        None,
    )


def _known_exit_cost(obs: Observation, start: tuple[int, int]) -> int | None:
    """Return known minimum terrain cost to exit, or None until it is usable."""
    if obs.exit_position is None:
        return None
    _, cost = dijkstra_path(obs, start, obs.exit_position)
    return None if cost >= _INFINITY else cost


def _remember_treasure_value(treasure: TreasureInfo) -> None:
    """Expose each observed value once through the student's policy state."""
    if treasure.value is None or treasure.position in _PLANNER_STATE["seen_treasure_values"]:
        return
    _PLANNER_STATE["seen_treasure_values"].add(treasure.position)
    _POLICY_STATE["observed_values"].append(treasure.value)


def _best_frontier_option(
    obs: Observation,
) -> tuple[tuple[int, int], list[Action], int, int | None] | None:
    """Pick the cheapest reachable, unvisited frontier in the known map.

    If the exit is already visible, routes used for exploration are forbidden
    from crossing it because entering E terminates the run immediately.
    """
    forbidden = () if obs.exit_position is None else (obs.exit_position,)
    ranked = []
    for frontier in known_frontiers(obs):
        if frontier in _PLANNER_STATE["visited"] or frontier == obs.exit_position:
            continue
        route, travel_cost = dijkstra_path(obs, obs.position, frontier, forbidden)
        if travel_cost >= _INFINITY:
            continue
        exit_cost = _known_exit_cost(obs, frontier)
        ranked.append((travel_cost, frontier, route, exit_cost))
    if not ranked:
        return None
    travel_cost, frontier, route, exit_cost = min(
        ranked, key=lambda item: (item[0], item[1])
    )
    return frontier, route, travel_cost, exit_cost


def _choose_movement(obs: Observation) -> Action:
    """Provided frontier exploration and online replanning."""
    _PLANNER_STATE["visited"].add(obs.position)
    option = _best_frontier_option(obs)

    # Finding the exit is infrastructure, not a student TODO. Until it is
    # revealed, always continue toward the next reachable frontier.
    if obs.exit_position is None:
        if option is not None and option[1]:
            return option[1][0]
        return safe_known_move(obs)

    # Once the exit is known, the student decides whether one more exploration
    # leg is worth its exact known travel-and-return energy.
    if option is not None:
        frontier, route, travel_cost, frontier_to_exit = option
        if (
            frontier_to_exit is not None
            and should_continue_exploring(
                obs,
                frontier,
                travel_cost,
                frontier_to_exit,
                _POLICY_STATE,
            )
            and route
        ):
            return route[0]

    exit_route, _ = dijkstra_path(obs, obs.position, obs.exit_position)
    return exit_route[0] if exit_route else safe_known_move(obs)


def choose_action(obs: Observation) -> Action:
    """Fixed Observe -> Collect-or-Move dispatcher used by viewer/evaluator."""
    _reset_only_for_a_new_run(obs)

    treasure = _uncollected_treasure_here(obs)
    if treasure is not None:
        _remember_treasure_value(treasure)
        exit_cost = _known_exit_cost(obs, obs.position)
        if should_collect(obs, treasure, exit_cost, _POLICY_STATE):
            # COLLECT consumes one turn but does not move and does not reset any
            # state. The next call continues with the same policy memory.
            return Action.COLLECT

    action = _choose_movement(obs)
    if action not in _MOVE_ACTIONS:
        raise ValueError("The fixed planner must return one MOVE_* action")
    return action
