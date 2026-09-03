"""WEEK 2 THURSDAY — prize-collecting weighted graph TODOs."""

from treasure_explorer.model import Action, Observation, TreasureInfo
from policy_helpers import dijkstra_path, safe_known_move


def make_state() -> dict:
    return {"plan": None}


# ======================== STUDENT TODO 1 ========================
def plan_targets(obs: Observation, state: dict) -> list[tuple[int, int]]:
    """Return a feasible treasure order followed by the exit.

    Recommended decomposition:
    1. Dijkstra from start, every treasure, and exit.
    2. Search (visited_subset, last_target) states with subset DP,
       branch-and-bound, exact enumeration, or a justified beam search.
    3. Add 1 energy per collected treasure and reject over-budget plans.
    """
    return [obs.exit_position] if obs.exit_position is not None else []


# ======================== STUDENT TODO 2 ========================
def should_collect(obs: Observation, treasure: TreasureInfo, state: dict) -> bool:
    plan = state.get("plan") or []
    return bool(plan and plan[0] == obs.position)


# ===================== PROVIDED ORCHESTRATION ===================
def choose_movement(obs: Observation, state: dict) -> Action:
    if state["plan"] is None:
        state["plan"] = plan_targets(obs, state)
    while state["plan"] and state["plan"][0] == obs.position:
        state["plan"].pop(0)
    target = state["plan"][0] if state["plan"] else obs.exit_position
    route, _ = dijkstra_path(obs, obs.position, target)
    return route[0] if route else safe_known_move(obs)
