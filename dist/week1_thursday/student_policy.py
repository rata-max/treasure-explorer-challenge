"""WEEK 1 THURSDAY — Global Tree Optimization (difficulty 3/5). Guide: README.md

Edit only the TODO functions (small helper functions are fine).

Provided : bfs_path, route_to, route_length (never cross E) in policy_helpers
You write: TODO 1 plan_targets (called once), TODO 2 should_collect
Required : the EXACT optimum on all 8 maps (the tests know the scores) and
           at most 2 s of planning per map. Up to 12 treasures, so plain
           permutations are too slow: use budget-pruned search or subset DP.
           README section 3 walks through a DP table on a shared branch.
Grading  : exact method 30, optimum 25, time limit 10, greedy counterexample
           20, design note 15.
Tests    : tests/test_student_todo.py fails on the starter; make it pass.
"""

from treasure_explorer.model import Action, Observation, TreasureInfo
from policy_helpers import route_length, route_to, safe_known_move

Position = tuple[int, int]
COLLECT_COST = 1


def make_state() -> dict:
    # plan persists across MOVE and COLLECT turns. None means "not planned yet".
    return {"plan": None}


# ======================== STUDENT TODO 1 ========================
def plan_targets(obs: Observation, state: dict) -> list[Position]:
    """Return the treasures to collect, in visit order, followed by the exit.

    Called ONCE, on the first turn. Maximise
        score = 50 + sum(values collected) + energy left
              = 50 + obs.energy + sum(values) - energy(plan)
    subject to energy(plan) <= obs.energy, where
        energy(plan) = d(S, t1) + 1 + d(t1, t2) + 1 + ... + d(tk, E)
    and d = route_length (E is never crossed on the way to a treasure).

    Required: an EXACT method. Budget-pruned search over orders, or subset DP
    over states (visited_set, last_treasure) - see README for a worked table.
    Limit: must finish in 2 seconds on every released map (up to 12 treasures),
    so plain itertools.permutations over all treasures is too slow.
    """
    return [obs.exit_position]  # starter: go straight out


# ======================== STUDENT TODO 2 ========================
def should_collect(obs: Observation, treasure: TreasureInfo, state: dict) -> bool:
    """Collect only the next planned treasure.

    The route may walk over a treasure that the plan skipped; collecting it
    would spend 1 energy the plan did not budget for.
    """
    plan = state.get("plan") or []
    return bool(plan and plan[0] == obs.position)


# ===================== PROVIDED ORCHESTRATION ===================
def choose_movement(obs: Observation, state: dict) -> Action:
    if state["plan"] is None:
        state["plan"] = plan_targets(obs, state)

    # After COLLECT the position is unchanged and collected=True. Drop the
    # reached target; the fixed agent.py deliberately kept the same plan list.
    while state["plan"] and state["plan"][0] == obs.position:
        state["plan"].pop(0)

    target = state["plan"][0] if state["plan"] else obs.exit_position
    route = route_to(obs, obs.position, target)  # never walks through E
    return route[0] if route else safe_known_move(obs)
