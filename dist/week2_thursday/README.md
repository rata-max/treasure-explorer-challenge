# Week 2 Thursday — Prize-Collecting Weighted Graph

한국어 공통 안내: `STUDENT_GUIDE_KO.md`

## Start here

1. Read `STUDENT_GUIDE.md` and run the safe starter.
2. Edit only `student_policy.py`.
3. Build pairwise Dijkstra costs, then implement `plan_targets`.
4. Keep the exit as the final target and include one energy per collection.

## File boundary

- **Edit and submit:** `student_policy.py`
- **Fixed:** `agent.py` viewer/evaluator adapter
- **Provided:** `policy_helpers.py` weighted path routines
- **Do not edit:** engine, viewer, runner, maps, tests

The fixed adapter separates `COLLECT` from movement and preserves the same `plan`
after collection. Do not reset the plan because the grid cell still displays `T`.

## Search policy

- Required: weighted shortest paths plus treasure subset/order optimization.
- Allowed: subset DP, exact enumeration, branch-and-bound, beam search, or another
  justified rule within the runtime limit.
- PyTorch, NumPy, learned models, external packages, hardcoding, file/network
  access, reflection, and subprocesses are forbidden.

## Maps and commands

`budget_tradeoff.json`, `cyclic_order.json`, `graph_challenge.json`,
`pair_or_prize.json`, `terrain_bundle.json`.

```powershell
python -m treasure_explorer --map maps/pair_or_prize.json --agent agent.py --view
Get-ChildItem maps/*.json | ForEach-Object { python -m treasure_explorer --map $_.FullName --agent agent.py }
python -m unittest discover -s tests -v
```
