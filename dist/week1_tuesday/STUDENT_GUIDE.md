# Student guide: edit the policy, not the engine adapter

## Files

| File/folder | May I edit it? | Purpose |
|---|---|---|
| `student_policy.py` | **Yes** | The only submitted file and the place for your rules/search |
| `agent.py` | **No** | Fixed viewer/evaluator adapter and per-run state lifecycle |
| `policy_helpers.py` | Normally no | Provided BFS, Dijkstra, frontier, and movement helpers |
| `treasure_explorer/` | No | Engine, model, runner, and viewer |
| `maps/` | No | Stage inputs |
| `tests/` | No | Contract and package checks |

The viewer needs the fixed `choose_action` in `agent.py`. Your policy supplies
`make_state`, `should_collect`, and `choose_movement` from `student_policy.py`.

## One action is one turn

`choose_action(observation)` is called again after every action. Local variables
inside a function disappear after the call; values stored in the `state` object
survive until the current map run ends.

Treasure collection takes three decision points:

1. Move onto `T`: the treasure is present but not collected.
2. The fixed adapter calls `should_collect`; returning `True` emits `COLLECT`.
3. Position is unchanged, energy decreases by 1, and the next observation marks
   `TreasureInfo.collected=True`. The same state/DFS stack is still available.

The grid character remains `T` after collection. Never use `grid[r][c] == "T"`
as the collected flag. Use the `TreasureInfo.collected` field.

## State reset rule

State resets only when a new map run starts (`turn == 0` or the turn number moves
backward). Do not clear `visited`, `parent`, a DFS stack, or a planned route merely
because the agent reached or collected a treasure.

## Dependencies and algorithms

- Python 3.11+ standard library only. PyTorch, NumPy, learned models, external
  packages, file access, networking, and subprocesses are not allowed.
- Map names, fixed coordinates, seeds, and memorized layouts are not valid rules.
- The stage README states the required and permitted search algorithms.

## Quick debugging checklist

- Does every call return one `Action.MOVE_*` or a collection decision through
  `should_collect`?
- Is the exit reachable with the remaining energy after collection?
- Does the route survive the extra, non-moving `COLLECT` turn?
- Are `?` cells treated as unknown rather than known floor?
- Does `python -m unittest discover -s tests -v` pass?
