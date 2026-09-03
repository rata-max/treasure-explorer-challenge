"""WEEK 1 THURSDAY — global tree planning TODOs."""

from treasure_explorer.model import Action, Observation, TreasureInfo
from policy_helpers import bfs_path, safe_known_move


def make_state() -> dict:
    # plan persists across MOVE and COLLECT turns. None means "not planned yet".
    return {"plan": None}


# ======================== STUDENT TODO 1 ========================
def plan_targets(obs: Observation, state: dict) -> list[tuple[int, int]]:
    """Return treasure positions in visit order, followed by the exit.

    Rule example: evaluate the complete route
      start -> treasure A -> treasure B -> ... -> exit
    instead of adding independent round trips. Shared tree edges are then paid only
    when the route actually traverses them. Exact subset/order search, tree DP, or
    branch-and-bound are suitable here.
    """
    return [obs.exit_position] if obs.exit_position is not None else []


# ======================== STUDENT TODO 2 ========================
def should_collect(obs: Observation, treasure: TreasureInfo, state: dict) -> bool:
    """Collect only if the current position is the next planned treasure."""
    plan = state.get("plan") or []
    return bool(plan and plan[0] == obs.position)


# ===================== PROVIDED ORCHESTRATION ===================
def choose_movement(obs: Observation, state: dict) -> Action:
    if state["plan"] is None:
        state["plan"] = plan_targets(obs, state)

    # After COLLECT, position is unchanged and collected=True. Remove the reached
    # target here; the fixed adapter deliberately preserved the same plan object.
    while state["plan"] and state["plan"][0] == obs.position:
        state["plan"].pop(0)

    target = state["plan"][0] if state["plan"] else obs.exit_position
    route = bfs_path(obs, obs.position, target)
    return route[0] if route else safe_known_move(obs)
