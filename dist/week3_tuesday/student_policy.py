"""WEEK 3 TUESDAY FINAL — Online exploration under fog (difficulty 5/5). Guide: README.md

Edit only this file: the two TODO functions, the constants, and any helper
functions you add. The fixed agent.py builds the options and walks the route.

Provided : Option list (frontiers + seen treasures with exact known costs),
           Dijkstra movement that never crosses E, exit_cost(obs)
You write: TODO 1 should_collect (handle exit_cost is None)
           TODO 2 choose_target (steer the search, decide when to leave)
Safety   : nothing stops you from running out of energy. Check
           cost_to + cost_to_exit + SAFETY_MARGIN <= energy yourself.
Measure  : python evaluate.py --seeds 100-299 (tune) and --seeds 0-99 (report)
Minimum  : seeds 0-29 mean >= 200, exit rate >= 90 %, 0 invalid actions
           (starter 166.8 / 90 %). Private evaluation: unpublished seeds of
           treasure_explorer/generator.py plus hand-made maps.
Grading  : private score 35, exit rate + invalid 15, experiments 20,
           design note + presentation 20, code quality 10.
"""

from treasure_explorer.model import Observation, TreasureInfo
from policy_helpers import Option, exit_cost  # exit_cost(obs) = known energy here -> E, or None


# Constants you may tune. Explain every value you choose in the design note.
SAFETY_MARGIN = 3


# ======================== STUDENT TODO 1 ========================
def should_collect(
    obs: Observation,
    treasure: TreasureInfo,
    exit_cost: int | None,
    state: dict,
) -> bool:
    """You are standing on an uncollected treasure. Return True to COLLECT.

    Inputs:
    - ``treasure.value``: revealed now that you stand on it (never None here)
    - ``exit_cost``: known energy from here to E, or **None while E is unseen**
    - ``state["observed_values"]``: every value revealed so far in this run

    Think in two separate parts:
    - profit: the move here is already paid; COLLECT costs exactly 1 energy
      (= 1 point), so the gain is ``value - 1``. Treasures never compete for
      that energy, so comparing with other values is NOT a reason to skip.
    - feasibility: afterwards you must still reach E. If ``exit_cost`` is a
      number, require ``obs.energy - 1 >= exit_cost + SAFETY_MARGIN``. If it
      is None you cannot know the exit cost: decide (and justify) a reserve.
    """
    return False  # starter: never collects


# ======================== STUDENT TODO 2 ========================
def choose_target(
    obs: Observation,
    options: tuple[Option, ...],
    state: dict,
) -> Option | None:
    """Pick where to go next, or return None to walk to the exit.

    Called every turn (the agent re-plans from the newest observation).
    ``options`` holds every reachable frontier and seen uncollected treasure,
    sorted by ``cost_to``; see ``Option`` in policy_helpers.py for the fields.

    - While E is unseen, returning None means "let the fixed rule pick the
      cheapest frontier". Returning an option lets YOU steer the search
      (e.g. prefer frontiers with many unknown cells, or a hidden treasure).
    - Once E is seen, returning None walks straight to E and ends the run.
      Before choosing an option, check that
          option.cost_to + option.cost_to_exit + SAFETY_MARGIN <= obs.energy
      because nothing else will stop you from running out of energy.

    A strong policy estimates, for each option, the expected points gained
    minus the EXTRA energy compared with leaving now:
        extra = option.cost_to + option.cost_to_exit - exit_cost(obs)
    The expected value of a hidden treasure or of an unexplored area has to be
    estimated from what this run has observed so far. The private maps come
    from the generator described in treasure_explorer/generator.py.
    """
    return None  # starter: cheapest frontier until E is seen, then exit
