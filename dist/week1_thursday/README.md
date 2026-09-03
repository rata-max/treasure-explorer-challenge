# Week 1 Thursday — Global Tree Optimization

한국어 공통 안내: `STUDENT_GUIDE_KO.md`

## Start here

1. Run the tests and the safe starter.
2. Read `STUDENT_GUIDE.md`.
3. Edit only `student_policy.py`, beginning with `plan_targets`.
4. Compare complete route scores across all five maps.

## File boundary

- **Edit and submit:** `student_policy.py`
- **Fixed:** `agent.py` (viewer/evaluator and state lifecycle)
- **Provided helper:** `policy_helpers.py` (BFS and path reconstruction)
- **Never edit:** engine, viewer, runner, maps, and tests

`plan` persists across movement and collection turns. When the agent collects on
`T`, the fixed wrapper does not clear the list. On the next call, the provided
orchestration removes the completed target and continues to the next one.

## Your TODOs

1. `plan_targets`: return selected treasures in visit order and append the exit.
2. `should_collect`: normally collect only the next planned treasure.

Evaluate `start -> selected treasures -> exit` as one expedition. Branches can
share edges, so independent treasure round trips give the wrong cost.

## Search policy

- Required: global treasure subset and visit-order reasoning.
- Allowed: exact enumeration, tree DP, subset DP, branch-and-bound, or a justified
  heuristic. BFS/DFS may be used for pairwise tree paths.
- Forbidden: map fingerprints/hardcoding, PyTorch/NumPy/external packages, file or
  network access, subprocesses, and learned models.

## Maps

`shared_branch.json`, `value_trap.json`, `subset_order.json`, `large_tree.json`,
and `challenge.json`.

```powershell
python -m treasure_explorer --map maps/shared_branch.json --agent agent.py --view
Get-ChildItem maps/*.json | ForEach-Object { python -m treasure_explorer --map $_.FullName --agent agent.py }
python -m unittest discover -s tests -v
```
