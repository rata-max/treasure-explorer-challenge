"""WEEK 3 TUESDAY FINAL — edit only the two marked decision rules.

The fixed ``agent.py`` already handles fog, persistent state, frontier search,
Dijkstra routing, online replanning, exit avoidance, and COLLECT lifecycle.
Your job is to design a general rule for hidden values and safe exploration.
"""

from treasure_explorer.model import Observation, TreasureInfo


# You may tune constants or add small helper functions in this student section.
SAFETY_MARGIN = 3


# ======================== STUDENT TODO 1 ========================
def should_collect(
    obs: Observation,
    treasure: TreasureInfo,
    exit_cost: int | None,
    state: dict,
) -> bool:
    """Return True only when collecting is valuable and a safe exit remains.

    Inputs prepared by the fixed adapter:
    - ``treasure.value``: revealed value because the agent is on the T cell
    - ``exit_cost``: minimum known energy from here to E, or None if E is hidden
    - ``state["observed_values"]``: values seen so far in this run

    Rule template (choose and justify your own threshold/margin):
        enough_energy = energy >= 1 COLLECT + exit_cost + safety_margin
        worth_it = value is large enough compared with observed values
        return enough_energy and worth_it
    """
    return False  # Safe starter: leave treasures untouched until you add a rule.


# ======================== STUDENT TODO 2 ========================
def should_continue_exploring(
    obs: Observation,
    frontier: tuple[int, int],
    cost_to_frontier: int,
    cost_frontier_to_exit: int,
    state: dict,
) -> bool:
    """Decide whether to visit one more frontier instead of exiting now.

    The fixed adapter calls this only after E is known and provides exact costs
    through currently known cells. A minimal safe rule compares

        cost_to_frontier + cost_frontier_to_exit + safety_margin

    with ``obs.energy``. Stronger rules may also use observed treasure values,
    remaining frontiers, or a larger risk margin. Do not use map names, fixed
    coordinates, dimensions, seeds, or memorized practice layouts.
    """
    return False  # Safe starter: exit immediately after the exit is discovered.
