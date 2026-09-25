# Student guide (Weeks 1–2): edit the policy, not the engine adapter

This assignment assumes Python functions, conditionals, lists and dictionaries,
and the graph algorithm of the current week. You run `--agent agent.py`, but the
**only file you edit and submit is `student_policy.py`**.

## Files

| File/folder | May I edit it? | Purpose |
|---|---|---|
| `student_policy.py` | **Yes** | Your rules and search code |
| `agent.py` | No | Viewer/evaluator adapter, per-run state, COLLECT handling |
| `policy_helpers.py` | No | Neighbour helper and, depending on the week, reference BFS/Dijkstra |
| `treasure_explorer/` | No | Engine, model, runner, viewer |
| `maps/`, `tests/` | No | Stage inputs and checks |

Evaluation replaces every fixed file with a clean official copy.

## Score and energy

On exit: `score = 50 + treasure collected + energy left − 5 × invalid actions`;
no exit means 0. **Spending less energy is itself score**, so a treasure is worth
`value − the extra energy it costs you`.

- Entering a cell costs: normal/S/E/T 1, mud M 4, water W 7. `COLLECT` costs 1.
- Entering E ends the run immediately. **A route to a treasure must not cross E.**
- Reaching 0 energy anywhere except E ends the run with 0. A move without enough
  energy, into a wall, or a COLLECT without treasure is invalid (−5, nothing changes).
- At most 500 turns.

## Path-function contract (every week)

| Case | BFS | Dijkstra |
|---|---|---|
| start == goal | `[]` | `([], 0)` |
| unreachable or goal `None` | `None` | `(None, None)` |
| otherwise | minimum-step route | (minimum-energy route, cost) |

## One action is one turn

`choose_action(observation)` is called again after every action. Local variables
disappear after the call; values stored in `state` survive until the map run ends.
The fixed adapter resets `state` only when a new run starts (`turn == 0` or the
turn number goes backwards).

**When do you need state?** A policy that recomputes its route every turn (like the
provided orchestration) needs no stored route. A policy that plans once on the first
turn (Thursdays) must keep that plan in `state["plan"]`. Never clear `state` just
because a treasure was reached or collected.

Collection takes three decision points:

1. Move onto `T`: the treasure is present but not collected.
2. The fixed adapter calls `should_collect`; returning `True` emits `COLLECT`.
3. Position is unchanged, energy drops by 1, and the next observation marks
   `TreasureInfo.collected=True`. The same `state` is passed again.

The grid character stays `T` after collection. Never use `grid[r][c] == "T"` as
the collected flag.

## Algorithms by stage

| Stage | You implement | Provided |
|---|---|---|
| Week 1 Tue | BFS with parent recovery (graded), single-detour rule | neighbours, reference BFS (fallback) |
| Week 1 Thu | subset search (pruned DFS or DP) | BFS |
| Week 2 Tue | Dijkstra (heap), energy-based detour rule | neighbours, BFS for comparison |
| Week 2 Thu | budgeted optimisation on weighted graphs (DP + pruning) | Dijkstra |
| Week 3 Tue | exploration strategy under fog, with experiments | options, Dijkstra movement |
| Week 3 Thu | **presentations only** (no new code) | — |

Python 3.11+ standard library only. No PyTorch, NumPy, learned models, external
packages, file access, networking or subprocesses. Map names, coordinates, seeds
and memorised layouts are not valid rules.

## What the tests mean

- `test_fixed_files`, `test_package`, `test_student_contract` check the environment
  and call contract and pass from the start (also on a Windows `git clone`).
- `test_student_todo` checks **your TODOs** and fails on the starter by design.
- Passing every test is a minimum, not a guarantee of a high grade. Report per-map
  score, exit, invalid actions and the limits of your policy.
