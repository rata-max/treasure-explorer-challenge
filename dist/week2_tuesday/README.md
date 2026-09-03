# Week 2 Tuesday — Weighted Graph Routes

한국어 공통 안내: `STUDENT_GUIDE_KO.md`

## Start here

Run the tests, view `terrain_choice.json`, then edit only `student_policy.py`.
`policy_helpers.dijkstra_path` is a provided, commented reference; your work is to
use true route costs in `select_target` and `should_collect`.

## File boundary

- **Edit and submit:** `student_policy.py`
- **Do not edit:** fixed `agent.py`, `policy_helpers.py`, engine, maps, tests
- Read `STUDENT_GUIDE.md` for the `T -> COLLECT -> resume` state sequence.

## Your TODOs

1. Select a treasure only when
   `start->treasure + COLLECT + treasure->exit` is feasible and profitable.
2. Use terrain-entry energy, not number of steps.

Terrain costs: normal/start/exit/treasure 1, mud 4, water 7. `COLLECT` costs 1.
Entering the exit ends the run, so it cannot be an intermediate waypoint.

## Search policy

- Required: Dijkstra or uniform-cost search for weighted routes.
- A* is allowed only with a documented admissible heuristic; a Dijkstra/UCS result
  must still be explainable for grading.
- No BFS-by-step-count for weighted cost decisions.
- Standard library only; no NumPy, PyTorch, learned models, hardcoding, file access,
  networking, or subprocesses.

## Maps and commands

`terrain_choice.json`, `cycle_detour.json`, `water_crossing.json`, `weighted_maze.json`.

```powershell
python -m treasure_explorer --map maps/terrain_choice.json --agent agent.py --view
Get-ChildItem maps/*.json | ForEach-Object { python -m treasure_explorer --map $_.FullName --agent agent.py }
python -m unittest discover -s tests -v
```
