# Week 1 Tuesday — 트리 계획 기초 (BFS 직접 구현)

난이도 ★★☆☆☆ · 3시간 실습 · 공통 안내: `STUDENT_GUIDE_KO.md` / `STUDENT_GUIDE.md`

**선수지식:** Python 함수·리스트·딕셔너리·튜플, 큐(`collections.deque`), BFS의 개념.
이번 주에는 BFS를 **직접 구현**합니다. 막혀도 과제 전체가 멈추지 않도록 동작하는 참고 BFS(`reference_bfs_path`)를 함께 제공합니다.
starter는 참고 BFS로 처음부터 실행되고, 여러분의 BFS는 따로 채점합니다.

## 1. 수정 범위

| 파일 | 수정 | 설명 |
|---|---|---|
| `student_policy.py` | **수정·제출** | TODO 1–3과 직접 만든 보조 함수 |
| `agent.py`, `policy_helpers.py`, `treasure_explorer/`, `maps/`, `tests/` | 금지 | 평가 시 공식 사본으로 교체됩니다 |

실행은 항상 `--agent agent.py`로 하지만, 제출 파일은 `student_policy.py` 하나입니다.

## 2. 먼저 이해할 것: 남은 에너지 = 점수

탈출했을 때 점수는 `50 + 수집한 보물 가치 + 남은 에너지 − 5 × 무효 행동`입니다(탈출 못 하면 0점).
**에너지 1을 쓰면 점수 1이 깎이므로**, 보물 하나의 순이익은 다음과 같습니다.

```
순이익 = 보물 가치 − (그 보물 때문에 추가로 쓴 에너지)
```

예시: 바로 출구로 가면 8. 보물까지 3, 보물에서 출구까지 9, 수집 1이면 전체 비용은 13.
추가 비용은 13 − 8 = 5이고, 보물 가치가 8이면 순이익은 3이므로 갑니다.
단, 남은 에너지가 13 이상일 때만 후보가 됩니다. 가치가 5 이하라면 가지 않는 것이 이득입니다.

그 밖의 규칙:
- 이동할 때마다 에너지 1(1주차 맵은 모두 비용 1 지형), `COLLECT`도 에너지 1. 보물 위에 도착해도 자동 수집되지 않습니다.
- **출구 E에 들어가는 순간 게임이 끝납니다.** 보물로 가는 경로가 E를 지나가면 그 자리에서 종료되므로 E를 벽처럼 취급해야 합니다.
- 출구가 아닌 칸에서 에너지가 0이 되면 즉시 종료(0점)입니다. 에너지가 모자란 이동은 무효 행동(−5점)입니다.

## 3. Observation 한눈에 보기

| 필드 | 뜻 |
|---|---|
| `position` | 현재 칸 `(row, col)`. `row`는 위에서 아래(0부터), `col`은 왼쪽에서 오른쪽 |
| `grid` | 문자열 튜플. `obs.grid[row][col]`로 읽습니다. `# . S E T` (1주차) |
| `exit_position` | 출구 좌표 |
| `energy` | 남은 에너지 |
| `treasures` | `TreasureInfo(position, value, collected)` 목록 |

수집한 뒤에도 격자 문자는 계속 `T`입니다. 수집 여부는 반드시 `TreasureInfo.collected`로 확인하세요.

## 4. TODO

### TODO 1 `bfs_path(obs, start, goal, forbidden=())`
완성하면 파일 위쪽의 `USE_MY_BFS = False`를 `True`로 바꾸세요. 그러면 에이전트가 참고 BFS 대신 여러분의 BFS로 움직입니다.
TODO 2·3을 먼저 하고 싶다면 `False`로 둔 채 진행해도 됩니다. 단, **`False`로 제출하면 20점 감점**입니다(7절).

- `start == goal` → `[]` (이미 도착, 이동 0번)
- 도달 불가능하거나 `goal is None` → **`None`** (`[]`와 구분됩니다)
- 그 외 → 최소 이동 횟수 경로의 `Action` 리스트
- 벽 `#`, 미지 `?`, `forbidden`의 칸에는 들어가지 않습니다.

구현 순서: `deque` 큐, `parent[다음칸] = (이전칸, 행동)` 딕셔너리, 목표에서 `parent`를 따라 거꾸로 올라가 경로를 복원한 뒤 뒤집기.
이웃은 `known_neighbors(obs, cell, forbidden)`이 `(다음칸, 행동, 비용)`으로 알려 줍니다.

`bfs_path` 안에서 `reference_bfs_path`를 그대로 부르면 점수가 없습니다. BFS 테스트는 참고 BFS를 막아 둔 상태로 여러분의 함수를 검사합니다.

제공 함수 `route_length(obs, a, b)`는 스위치가 고른 BFS를 불러, **목표가 E가 아니면 E를 금지 칸으로 넣은** 경로 길이를 돌려줍니다.

### TODO 2 `should_collect(obs, treasure, state)`
가치가 1보다 크고, 수집(1) 후에도 `route_length(현재, E)`만큼 에너지가 남으면 `True`.

### TODO 3 `select_target(obs, state)` — 단일 우회 규칙(필수 수준)
보물 t마다 `extra = d(현재,t) + 1 + d(t,E) − d(현재,E)`, `gain = 가치 − extra`를 계산합니다.
`gain`이 가장 큰 양수이고 전체 비용 `d(현재,t) + 1 + d(t,E)`가 에너지 이하인 보물을 고르고, 없으면 출구를 고릅니다.
제공 orchestration이 매 턴 이 함수를 다시 부르므로, 수집 후에는 자동으로 다음 목표를 고릅니다.

**보너스(선택):** 여러 보물의 **방문 순서**까지 고려하면 두 맵의 점수가 오릅니다. 목요일 주제의 예고편입니다.

## 5. 맵과 기준 점수

| 맵 | 배울 점 | 직행(탈출만) | 필수 수준(단일 우회) | 보너스(순서 고려) = 최적 |
|---|---|---:|---:|---:|
| `warmup.json` | 경로 위 보물 | 60 | 67 | 67 |
| `two_branches.json` | 두 갈래 비교 | 76 | 88 | 90 |
| `greedy_trap.json` | 가장 가까운 것이 최선은 아님 | 63 | 78 | 78 |
| `energy_budget.json` | 출구 에너지 예약 | 66 | 78 | 84 |

`two_branches`와 `energy_budget`에서 필수 수준이 최적에 못 미치는 것은 **의도된 결과**입니다.
보물을 하나씩만 보면 순서 문제를 풀 수 없습니다. 설계 노트에 그 이유를 한 문단으로 적으면 됩니다.

## 6. 테스트

```powershell
python -m unittest discover -s tests -v
```

- `test_fixed_files`, `test_package`, `test_student_contract`: 환경·계약 확인. 처음부터 통과합니다.
- `test_student_todo`: **여러분의 TODO를 검사합니다. starter에서는 실패하는 것이 정상**입니다.
  - `BfsTests`(5개): 여러분의 `bfs_path`만 검사합니다(참고 BFS는 막힘).
  - `test_submission_uses_my_bfs`: 제출본이 `USE_MY_BFS = True`인지 확인합니다. 실패한 채로 제출하면 20점 감점입니다.
  - `DecisionTests`, `FullRunTests`: 수집·우회 판단과 4개 맵 완주. `USE_MY_BFS`가 고른 BFS를 쓰므로, BFS를 못 짜도 참고 BFS로 통과할 수 있습니다.
- 테스트 통과는 최소 조건입니다. 점수표와 설계 노트도 채점합니다.

> 게임 점수로는 BFS를 직접 짰는지 구분할 수 없습니다. 참고 BFS도 정확하기 때문입니다. 그래서 BFS 구현은 `BfsTests`와 코드 검토로만 채점합니다.

## 7. 제출물과 채점(100점)

제출물: `student_policy.py`(**`USE_MY_BFS = True`**), 1쪽 설계 노트(BFS 시간복잡도 O(V+E)와 그 이유, 4개 맵 점수표, 필수 수준이 최적에 못 미치는 맵의 원인).

| 항목 | 점수 |
|---|---:|
| **직접 작성한 BFS로 실행** (`BfsTests`, 부분 점수): 계약 `[]`/`None` 4 · 최단 경로 8 · 금지 칸 4 · 미지 칸 4 | 20 |
| 수집·목표 판단 규칙(`DecisionTests` + 코드 검토) | 30 |
| 4개 맵 안전 완주(탈출, 무효 행동 0) | 20 |
| 점수(필수 수준 도달 15, 보너스는 가산 최대 +5) | 15 |
| 설계 노트 | 15 |

> **기본 코드만으로 제출하면 20점 감점**
> 제출한 에이전트가 제공된 `reference_bfs_path`로만 움직이면 위 BFS 항목 20점을 모두 잃습니다. 다음 두 경우가 해당합니다.
> - `USE_MY_BFS = False` 상태로 제출(내 BFS를 짰더라도 스위치를 켜지 않으면 해당)
> - `bfs_path`가 `reference_bfs_path`를 그대로 호출하거나 감싸기만 한 경우
>
> 감점은 이 한 항목에서만 적용되며 중복되지 않습니다. 이 경우에도 나머지 80점은 받을 수 있습니다.
> `test_submission_uses_my_bfs`가 실패하면 스위치가 꺼진 상태입니다.

`BfsTests`가 통과해도 코드 검토에서 BFS가 아니면(예: DFS로 우연히 통과) 해당 테스트의 부분 점수는 인정하지 않습니다.

## 8. 3시간 운영안

| 시간 | 활동 |
|---|---|
| 0–20분 | 점수식·Observation·COLLECT 설명, starter 실행 |
| 20–80분 | TODO 1 BFS 구현, `BfsTests` 통과 후 `USE_MY_BFS = True` (80분까지 막히면 `False`로 두고 다음 단계로) |
| 80–90분 | 휴식 |
| 90–130분 | TODO 2·3 구현 |
| 130–160분 | 4개 맵 실행, 점수표 작성, (선택) 보너스 |
| 160–180분 | 설계 노트, 제출 점검(`USE_MY_BFS = True` 확인) |

starter는 참고 BFS로 출구까지 곧장 갑니다(보물은 줍지 않음). `USE_MY_BFS = True`로 바꿨는데 `NotImplementedError`가 나면 TODO 1이 아직 비어 있는 것입니다.

## 9. 명령어

```powershell
python -m treasure_explorer --map maps/warmup.json --agent agent.py --view
Get-ChildItem maps/*.json | ForEach-Object { python -m treasure_explorer --map $_.FullName --agent agent.py }
python -m unittest discover -s tests -v
```

허용: Python 3.11+ 표준 라이브러리. 금지: 맵 이름·좌표 하드코딩, 외부 패키지(NumPy·PyTorch 등), 파일·네트워크·subprocess 접근.
