# Student guide: Week 3 partial-observation final

The task, grading and schedule are in `README.md` (Korean). This guide lists the
concepts and the common mistakes. All code is written, tested and submitted in the
three-hour Tuesday session; Thursday is presentations only.

## File versus Observation

Map files (and generator output) contain the ground truth because the engine needs
it. The `Observation` your code receives is masked: unseen cells are `?` (never
assume they are floor), unreached treasure values are `None`, and `exit_position`
is `None` until E is seen. With `reveal_radius` 1 every step reveals the cells at
Manhattan distance 1.

## Terms

- **frontier**: a *known walkable* cell next to at least one `?` (not the unknown cell).
- **cost_to_exit**: one-way energy from the option to E (not a round trip back here).
- **extra energy**: `cost_to + cost_to_exit − exit_cost(obs)`, i.e. how many points
  visiting the option costs compared with leaving now.

## Common mistakes

1. Computing `1 + exit_cost + margin` when `exit_cost is None` (TypeError).
2. Skipping a treasure because it is below the average: standing on it, COLLECT
   costs 1, so any value above 1 is profit if the exit stays affordable.
3. Picking an option after E is known without checking the way back. The fixed code
   will not stop you.
4. Switching goals every turn and oscillating. Remember the goal in `state`.
5. Tuning constants on one public map. Use `evaluate.py` with separate tuning and
   reporting seed ranges.
6. Using `grid[r][c] == "T"` as the collected flag. Use `TreasureInfo.collected`.

## The safety margin is a heuristic

It is energy you promise not to spend; it does not guarantee an exit. Once E is known
the known-map cost is exact, so a small margin suffices. Before E is known any reserve
is an estimate. Justify it in the design note.

## Public practice guarantees

Public maps and public seeds use the **same rules and parameter ranges** as the private
evaluation. They do not reveal private layouts, exits or values.

## Rules

Python 3.11+ standard library only; no external packages, learned models, file,
network, subprocess or reflection access; no branching on map names, coordinates,
sizes, shapes or seeds; no state shared between evaluation runs.
