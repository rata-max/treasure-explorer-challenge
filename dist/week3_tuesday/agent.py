"""Fixed online-planning adapter for the Week 3 final.

DO NOT EDIT OR SUBMIT THIS FILE.

What this file does for you, every turn:
  1. keeps per-run memory (reset only when a new map starts);
  2. if you stand on an uncollected treasure, reveals its value to
     ``state["observed_values"]`` and asks ``should_collect``;
  3. builds the list of ``Option``s (frontiers and seen treasures) with exact
     known-map energy costs, and asks ``choose_target`` which one to head for;
  4. takes ONE Dijkstra step toward that target. Routes never cross E unless
     E is the destination, and a step is never taken without enough energy.

Your decisions live in student_policy.py.
"""

from __future__ import annotations

from treasure_explorer.model import Action, Observation, TreasureInfo
from policy_helpers import (
    Option,
    TERRAIN_COST,
    costs_to,
    dijkstra_all,
    dijkstra_path,
    known_frontiers,
    safe_known_move,
    unknown_nearby,
)
from student_policy import choose_target, should_collect


_MOVE_ACTIONS = frozenset(
    {Action.MOVE_UP, Action.MOVE_DOWN, Action.MOVE_LEFT, Action.MOVE_RIGHT}
)
_STEP = {Action.MOVE_UP: (-1, 0), Action.MOVE_DOWN: (1, 0),
         Action.MOVE_LEFT: (0, -1), Action.MOVE_RIGHT: (0, 1)}
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
    # The grid character stays "T" after collection; ``collected`` is authoritative.
    return next(
        (t for t in obs.treasures if t.position == obs.position and not t.collected),
        None,
    )


def _remember_treasure_value(treasure: TreasureInfo) -> None:
    if treasure.value is None or treasure.position in _PLANNER_STATE["seen_treasure_values"]:
        return
    _PLANNER_STATE["seen_treasure_values"].add(treasure.position)
    _POLICY_STATE["observed_values"].append(treasure.value)


def build_options(obs: Observation) -> list[Option]:
    """All reachable frontiers and seen uncollected treasures, cheapest first."""
    exit_pos = obs.exit_position
    forbidden = () if exit_pos is None else (exit_pos,)
    reach, _ = dijkstra_all(obs, obs.position, forbidden)
    to_exit = {} if exit_pos is None else costs_to(obs, exit_pos)

    def exit_cost_from(cell):
        return to_exit.get(cell)

    options: list[Option] = []
    for cell in known_frontiers(obs):
        if cell == exit_pos or cell == obs.position or cell in _PLANNER_STATE["visited"]:
            continue
        if cell in reach:
            options.append(Option("frontier", cell, reach[cell], exit_cost_from(cell),
                                  unknown_nearby(obs, cell)))
    for t in obs.treasures:
        if t.collected or t.position == obs.position or t.position not in reach:
            continue
        options.append(Option("treasure", t.position, reach[t.position],
                              exit_cost_from(t.position), unknown_nearby(obs, t.position), t.value))
    options.sort(key=lambda o: (o.cost_to, o.kind, o.position))
    return options


def _affordable_first_step(obs: Observation, route: list[Action] | None) -> Action | None:
    if not route:
        return None
    dr, dc = _STEP[route[0]]
    r, c = obs.position[0] + dr, obs.position[1] + dc
    return route[0] if TERRAIN_COST[obs.grid[r][c]] <= obs.energy else None


def _choose_movement(obs: Observation) -> Action:
    _PLANNER_STATE["visited"].add(obs.position)
    options = build_options(obs)
    choice = choose_target(obs, tuple(options), _POLICY_STATE)

    if choice is not None and choice not in options:
        raise ValueError("choose_target must return one of the given options or None")

    if choice is None and obs.exit_position is None:
        # E unseen: exiting is impossible, so fall back to the cheapest frontier.
        choice = next((o for o in options if o.kind == "frontier"), None)

    if choice is None:
        goal, forbidden = obs.exit_position, ()
    else:
        goal = choice.position
        forbidden = () if obs.exit_position is None else (obs.exit_position,)
    route, _ = dijkstra_path(obs, obs.position, goal, forbidden)
    step = _affordable_first_step(obs, route)
    return step if step is not None else safe_known_move(obs)


def choose_action(obs: Observation) -> Action:
    """Fixed Observe -> Collect-or-Move dispatcher used by viewer/evaluator."""
    _reset_only_for_a_new_run(obs)

    treasure = _uncollected_treasure_here(obs)
    if treasure is not None:
        _remember_treasure_value(treasure)
        cost_home = dijkstra_path(obs, obs.position, obs.exit_position)[1]
        if obs.energy >= 1 and should_collect(obs, treasure, cost_home, _POLICY_STATE):
            # COLLECT consumes one turn, does not move and does not reset state.
            return Action.COLLECT

    action = _choose_movement(obs)
    if action not in _MOVE_ACTIONS:
        raise ValueError("The fixed planner must return one MOVE_* action")
    return action
