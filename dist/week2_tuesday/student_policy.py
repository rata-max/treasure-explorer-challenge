"""WEEK 2 TUESDAY — weighted-route TODOs."""

from treasure_explorer.model import Action, Observation, TreasureInfo
from policy_helpers import dijkstra_path, safe_known_move


def make_state() -> dict:
    return {"target": None}


# ======================== STUDENT TODO 1 ========================
def should_collect(obs: Observation, treasure: TreasureInfo, state: dict) -> bool:
    """Collect a treasure only when it is the selected target and exit remains safe."""
    return state.get("target") == obs.position


# ======================== STUDENT TODO 2 ========================
def select_target(obs: Observation, state: dict) -> tuple[int, int] | None:
    """Choose a treasure detour or the exit using true terrain-entry costs.

    Rule example: compare
      direct(start, exit)
    with
      cost(start, treasure) + 1 COLLECT + cost(treasure, exit).
    Use Dijkstra costs; step count is wrong when mud or water is present.
    """
    return obs.exit_position


# ===================== PROVIDED ORCHESTRATION ===================
def choose_movement(obs: Observation, state: dict) -> Action:
    if state["target"] is None or state["target"] == obs.position:
        state["target"] = select_target(obs, state)
    route, _ = dijkstra_path(obs, obs.position, state["target"])
    return route[0] if route else safe_known_move(obs)
