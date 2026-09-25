"""WEEK 2 THURSDAY — Prize-Collecting Weighted Graph (difficulty 4/5). Guide: README.md

Edit only the TODO functions (small helper functions are fine).

Provided : dijkstra_path, route_to, route_cost (never cross E) in policy_helpers
You write: TODO 1 plan_targets (called once), TODO 2 should_collect
Required : the EXACT optimum on all 8 maps within 5 s each. Budgets are tight
           and grand_tour.json has 15 treasures (order search takes ~20 s),
           so expand only DP states that can still reach E within budget.
Private  : two unreleased maps with 16-18 treasures, 10 s planning limit.
Grading  : exact method 30, optimum 20, time 10, ablation table 20,
           private stress maps 10, design note 10.
Tests    : tests/test_student_todo.py fails on the starter; make it pass.
"""

from treasure_explorer.model import Action, Observation, TreasureInfo
from policy_helpers import route_cost, route_to, safe_known_move

Position = tuple[int, int]
COLLECT_COST = 1


def make_state() -> dict:
    return {"plan": None}


# ======================== STUDENT TODO 1 ========================
def plan_targets(obs: Observation, state: dict) -> list[Position]:
    """Return the treasures to collect, in visit order, followed by the exit.

    Same objective as Week 1 Thursday, now on a CYCLIC WEIGHTED graph:
        maximise  sum(values) - energy(plan)   s.t.  energy(plan) <= obs.energy
        energy(plan) = c(S,t1) + 1 + c(t1,t2) + 1 + ... + c(tk,E),  c = route_cost

    What is new compared with Week 1 Thursday:
    - Costs come from Dijkstra (mud 4, water 7). Build the pairwise cost table
      once: 1 Dijkstra run per point, not one per pair (k+1 runs, not k^2).
    - Budgets are tight: the best plan often skips treasures whose single
      detour looks profitable (tight_budget.json, low_value_bait.json).
    - grand_tour.json has 15 treasures and a loose budget: enumerating orders
      (even with budget pruning) takes minutes. You need subset DP over
      (visited_set, last) that only expands states still within budget, or a
      branch-and-bound with a real upper bound.
    Limit: 5 seconds per map (tests/test_student_todo.py measures it).
    """
    return [obs.exit_position]  # starter: go straight out


# ======================== STUDENT TODO 2 ========================
def should_collect(obs: Observation, treasure: TreasureInfo, state: dict) -> bool:
    """Collect only the next planned treasure."""
    plan = state.get("plan") or []
    return bool(plan and plan[0] == obs.position)


# ===================== PROVIDED ORCHESTRATION ===================
def choose_movement(obs: Observation, state: dict) -> Action:
    if state["plan"] is None:
        state["plan"] = plan_targets(obs, state)
    while state["plan"] and state["plan"][0] == obs.position:
        state["plan"].pop(0)
    target = state["plan"][0] if state["plan"] else obs.exit_position
    route = route_to(obs, obs.position, target)  # never walks through E
    return route[0] if route else safe_known_move(obs)
