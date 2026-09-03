"""WEEK 1 TUESDAY — edit only the TODO functions in this file."""

from treasure_explorer.model import Action, Observation, TreasureInfo
from policy_helpers import bfs_path, safe_known_move


def make_state() -> dict:
    """Persistent values for one map run. The fixed adapter resets this safely."""
    return {"target": None}


# ======================== STUDENT TODO 1 ========================
def should_collect(obs: Observation, treasure: TreasureInfo, state: dict) -> bool:
    """Return True only when collection still leaves a safe route to the exit.

    Rule example (not a complete solution): collecting an on-route treasure costs
    1 energy. A detour also pays the movement out and back. Compare treasure.value
    with that complete extra cost, then reserve the BFS distance to the exit.
    """
    return False  # Safe starter: skip treasure until you implement the rule.


# ======================== STUDENT TODO 2 ========================
def select_target(obs: Observation, state: dict) -> tuple[int, int] | None:
    """Choose an uncollected treasure or the exit.

    Suggested steps:
    1. Recover the unique tree path to each treasure with BFS/DFS.
    2. Include movement, the 1-energy COLLECT action, and final exit distance.
    3. Choose only a target whose complete expedition fits obs.energy.
    """
    return obs.exit_position  # Provided safe baseline.


# ===================== PROVIDED ORCHESTRATION ===================
def choose_movement(obs: Observation, state: dict) -> Action:
    """Do not rewrite this first; improve the two TODO rules above."""
    state["target"] = select_target(obs, state)
    route = bfs_path(obs, obs.position, state["target"])
    return route[0] if route else safe_known_move(obs)
