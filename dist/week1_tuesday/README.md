# Week 1 Tuesday — Tree Planning Foundations

한국어 공통 안내: `STUDENT_GUIDE_KO.md`

## Start here (10 minutes)

1. Run `python -m unittest discover -s tests -v`.
2. Watch the safe starter: `python -m treasure_explorer --map maps/warmup.json --agent agent.py --view`.
3. Open **only `student_policy.py`** and read TODO 1–2.
4. Implement one rule at a time, then run every map.

Read `STUDENT_GUIDE.md` before coding. It explains the per-turn state model and
why collecting `T` must not clear a DFS stack or parent array.

## What may be edited?

- **Edit and submit:** `student_policy.py`
- **Do not edit:** `agent.py`, `policy_helpers.py`, `treasure_explorer/`, `maps/`, `tests/`
- The fixed `agent.py` keeps the viewer/API working, resets state only for a new
  run, and handles the non-moving `COLLECT` turn.

## Your two TODOs

1. `should_collect`: reserve enough energy for collection and the final exit.
2. `select_target`: compare each treasure's complete detour, not just its distance.

The provided `bfs_path` is a readable reference implementation with parent-based
path recovery. You may reimplement it with BFS or DFS in `student_policy.py` if
required by your instructor, but keep the fixed adapter unchanged.

## Search policy

- Required learning: BFS or DFS and parent/path recovery.
- Allowed: tree traversal, simple enumeration, energy-feasibility rules.
- Not allowed: map-name/coordinate hardcoding, external packages, NumPy, PyTorch,
  learned models, file/network/subprocess access.

## Maps

| Map | Lesson |
|---|---|
| `warmup.json` | Treasure on a useful route |
| `two_branches.json` | Compare branch detours |
| `greedy_trap.json` | Nearest is not always best |
| `energy_budget.json` | Reserve the exit cost |

Every move costs 1; `COLLECT` costs 1. Entering the exit ends the run, and no exit
means score 0.

## Commands

```powershell
python -m treasure_explorer --map maps/warmup.json --agent agent.py --view
Get-ChildItem maps/*.json | ForEach-Object { python -m treasure_explorer --map $_.FullName --agent agent.py }
python -m unittest discover -s tests -v
```
