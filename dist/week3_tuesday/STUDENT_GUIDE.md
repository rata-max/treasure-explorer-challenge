# Student guide: three-hour Tuesday integrated hidden final

This package follows Week 2 Thursday and completes all coding in one three-hour
Tuesday session. Thursday is presentation-only. The fixed adapter provides the
fog/frontier/replanning mechanics; students edit and submit only
`student_policy.py`.

## Practice file versus agent observation

`robustness_practice.json` is a public debugging file. Its raw JSON necessarily
contains the complete grid and actual treasure values so the local engine can
run. A student who opens the file can see that ground truth.

The `Observation` passed to the agent is different: unseen terrain is `?`, an
unreached treasure value is `None`, and the exit is `None` until revealed.
Therefore the public practice map simulates the partial-observation API; it is
not a secret file. Real hidden-map evaluation uses private map files that are
not distributed to students.

## File boundary

| File/folder | Editable? | Purpose |
|---|---|---|
| `student_policy.py` | **Yes** | Two policy decisions and student constants/helpers |
| `agent.py` | **No** | Viewer adapter, state, frontiers, Dijkstra, replanning |
| `policy_helpers.py` | **No** | Known-map route and frontier helpers |
| `treasure_explorer/` | No | Engine, model, runner, viewer |
| `maps/`, `tests/` | No | One public practice map and contract tests |

## Provided infrastructure

The fixed code maintains per-run state, distinguishes `?` from known terrain,
selects reachable frontiers, routes with Dijkstra, replans from each observation,
avoids crossing the terminal exit while exploring, and preserves state across
the non-moving COLLECT turn.

## Student TODOs

1. `should_collect`: compare revealed value, the 1-energy collection cost,
   known exit cost, and a safety margin.
2. `should_continue_exploring`: compare the supplied frontier travel/return
   costs with remaining energy and expected benefit.

The starter exits safely after finding the exit and collects nothing. Improve
its score without sacrificing generality or exit safety.

## 180-minute schedule

| Time | Activity |
|---|---|
| 0–20 | Instructor demo: fog, frontier, hidden values |
| 20–35 | Run starter and tests |
| 35–70 | Implement `should_collect` |
| 70–80 | Break |
| 80–125 | Implement `should_continue_exploring` |
| 125–155 | Test and tune on the public map |
| 155–175 | Record results and explain decisions |
| 175–180 | Submit `student_policy.py` |

Do not continue coding on Thursday; present the submitted Tuesday policy and
its results.

## Evaluation boundary

- Public: `maps/robustness_practice.json`
- Private: hidden-value maps and additional private seeds
- The exact same `student_policy.py` runs on every map.
- Standard library only. No PyTorch, NumPy, learned models, external packages,
  map fingerprints, hardcoded coordinates, files, network, subprocesses,
  reflection, side channels, or cross-run memory.

```powershell
python -m treasure_explorer --map maps/robustness_practice.json --agent agent.py --view
python -m unittest discover -s tests -v
```
