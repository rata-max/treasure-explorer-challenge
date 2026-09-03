"""Fixed engine adapter for Treasure Explorer.

DO NOT EDIT OR SUBMIT THIS FILE.

The viewer and evaluator load ``choose_action`` from this module. Student code
lives in ``student_policy.py``. Keeping the adapter fixed prevents accidental
viewer/API breakage and gives every map run a clean, persistent state object.
"""

from __future__ import annotations

from treasure_explorer.model import Action, Observation, TreasureInfo
from student_policy import choose_movement, make_state, should_collect


_MOVE_ACTIONS = frozenset(
    {Action.MOVE_UP, Action.MOVE_DOWN, Action.MOVE_LEFT, Action.MOVE_RIGHT}
)
_STATE = make_state()
_LAST_TURN: int | None = None


def _reset_only_for_a_new_run(obs: Observation) -> None:
    """Reset state at a map boundary, never after reaching/collecting treasure."""
    global _STATE, _LAST_TURN
    if _LAST_TURN is None or obs.turn == 0 or obs.turn <= _LAST_TURN:
        _STATE = make_state()
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


def choose_action(obs: Observation) -> Action:
    """Fixed Observe -> Collect-or-Move dispatcher used by the evaluator."""
    _reset_only_for_a_new_run(obs)

    treasure = _uncollected_treasure_here(obs)
    if treasure is not None and should_collect(obs, treasure, _STATE):
        # COLLECT consumes one turn but does not move the agent and does not
        # reset _STATE. The next call resumes the same plan/backtracking stack.
        return Action.COLLECT

    action = choose_movement(obs, _STATE)
    if action not in _MOVE_ACTIONS:
        raise ValueError(
            "choose_movement must return one MOVE_* Action; "
            "COLLECT is handled by the fixed agent adapter"
        )
    return action
