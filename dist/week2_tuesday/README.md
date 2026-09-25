# Week 2 Tuesday — 가중 그래프 경로 (Dijkstra 직접 구현)

난이도 ★★★☆☆ · 3시간 실습 · 공통 안내: `STUDENT_GUIDE_KO.md` / `STUDENT_GUIDE.md`

**선수지식:** 1주차 과제, 우선순위 큐(`heapq`), Dijkstra의 개념.
이번 주에는 Dijkstra를 **직접 구현**합니다. 지형마다 에너지가 다르므로 "이동 횟수가 적은 길"과 "에너지가 적은 길"이 달라집니다.

## 1. 지형과 비용

셀에 **들어갈 때** 비용을 냅니다: 일반·S·E·T = 1, 진흙 `M` = 4, 물 `W` = 7. `COLLECT` = 1.
점수 해석은 1주차와 같습니다. 남은 에너지 1 = 1점이므로 `순이익 = 가치 − 추가 에너지`입니다.

```
SMM.E      윗줄 직행: 4번 이동, 4 + 4 + 1 + 1 = 10 에너지
.....      아래 우회: 6번 이동, 6 에너지  ← Dijkstra가 골라야 하는 길
```

## 2. 수정 범위와 제공 코드

- **수정·제출:** `student_policy.py`
- **제공:** `known_neighbors`(이웃과 진입 비용), 비교용 `bfs_path`(이동 횟수 기준 — **가중치 판단에 쓰면 안 됨**)
- **수정 금지:** `agent.py`, `policy_helpers.py`, 엔진, 맵, 테스트

## 3. TODO

### TODO 1 `dijkstra_path(obs, start, goal, forbidden=())` → `(경로, 비용)`
- `start == goal` → `([], 0)` / 도달 불가·`goal is None` → `(None, None)`
- 비용 = 들어간 칸들의 진입 비용 합. 반환한 경로를 실제로 걸었을 때의 비용과 같아야 합니다(테스트가 검사).
- `heapq`로 `(비용, 칸)`을 넣고, **꺼낸 비용이 이미 기록된 최소 비용보다 크면 건너뜁니다**(같은 칸이 여러 번 들어가 있을 수 있음).
  `parent` 딕셔너리로 경로를 복원합니다. 목표 복잡도는 O((V+E) log V)입니다.

제공 함수 `route_cost(obs, a, b)`는 여러분의 Dijkstra를 부르되, 목표가 E가 아니면 **E를 금지 칸으로** 넣습니다.
제공 orchestration도 목표가 보물일 때 E를 지나지 않도록 `forbidden`을 넘깁니다.

### TODO 2 `should_collect` / TODO 3 `select_target`
1주차 화요일과 같은 단일 우회 규칙이되, 모든 거리를 `route_cost`(에너지)로 계산합니다.
**보너스(선택):** 방문 순서까지 고려하면 `cycle_detour`가 100 → 113점이 됩니다.

## 4. 맵과 기준 점수

| 맵 | 무엇을 시험하나 | 직행 | 필수 수준 | 보너스 = 최적 |
|---|---|---:|---:|---:|
| `terrain_choice.json` | 지형 선택 | 70 | 91 | 91 |
| `cycle_detour.json` | 사이클 우회 | 80 | 100 | 113 |
| `water_crossing.json` | 물은 짧아도 비쌈 | 80 | 99 | 99 |
| `weighted_maze.json` | 가중 경로 복원 | 84 | 106 | 106 |
| `mud_shortcut.json` | BFS로 판단하면 24점 손해 | 87 | 154 | 154 |
| `energy_illusion.json` | 이동 횟수로 예산을 재면 에너지가 바닥나 0점. **아무것도 줍지 않는 것이 최적** | 87 | 87 | 87 |
| `exit_in_the_way.json` | E가 보물 사이에 있음: E를 지나면 즉시 종료 | 65 | 92 | 92 |

BFS(이동 횟수)로 판단하는 정책은 `water_crossing` 81점, `mud_shortcut` 130점, `energy_illusion` 0점을 받습니다.
설계 노트의 비교표에 여러분의 결과를 적으세요.

## 5. 테스트

- `test_student_todo.py`: Dijkstra 계약(위 `SMM.E` 예시 포함), 금지 칸·미지 칸, 진흙을 지나는 우회의 가격, 에너지 기준 예산, E 경유 금지, 7개 맵의 필수 수준 점수. **starter에서는 실패가 정상**입니다.

## 6. 제출물과 채점(100점)

제출물: `student_policy.py`, 설계 노트(Dijkstra 복잡도와 stale 항목을 건너뛰는 이유, BFS 대 Dijkstra 7개 맵 비교표, `energy_illusion`에서 아무것도 줍지 않는 이유).

| 항목 | 점수 |
|---|---:|
| Dijkstra 구현(힙, stale 처리, 경로 복원, 계약) | 30 |
| 판단 규칙(에너지 기준 우회·예산·E 경유 금지) | 20 |
| 7개 맵 필수 수준 도달(탈출, 무효 행동 0) | 20 |
| BFS 대 Dijkstra 비교표와 분석 | 15 |
| 설계 노트 | 15 |

## 7. 3시간 운영안

| 시간 | 활동 |
|---|---|
| 0–20분 | 진입 비용 규칙, `SMM.E` 손 계산 |
| 20–80분 | TODO 1 Dijkstra, Dijkstra 테스트 통과 |
| 80–90분 | 휴식 |
| 90–130분 | TODO 2·3(1주차 코드를 `route_cost`로 교체) |
| 130–160분 | 7개 맵 실행, `bfs_path`로 바꿔 비교표 작성 |
| 160–180분 | 설계 노트, 제출 점검 |

```powershell
python -m treasure_explorer --map maps/terrain_choice.json --agent agent.py --view
Get-ChildItem maps/*.json | ForEach-Object { python -m treasure_explorer --map $_.FullName --agent agent.py }
python -m unittest discover -s tests -v
```

허용: Python 3.11+ 표준 라이브러리. A*는 허용 가능한(admissible) 휴리스틱을 설계 노트에 증명한 경우에만 허용합니다. 금지: 가중치 판단에 BFS 사용, 하드코딩, 외부 패키지, 파일·네트워크·subprocess 접근.
