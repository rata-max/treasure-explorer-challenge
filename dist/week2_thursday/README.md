# Week 2 Thursday — 상금 수집 가중 그래프 (예산 제약 최적화)

난이도 ★★★★☆ · 3시간 실습 · 공통 안내: `STUDENT_GUIDE_KO.md` / `STUDENT_GUIDE.md`

**선수지식:** 1주차 목요일(부분집합 DP), 2주차 화요일(Dijkstra).
1주차 목요일의 목적함수를 **사이클이 있는 가중 그래프**, **빠듯한 예산**, **더 큰 규모**로 확장합니다.

## 1. 1주차 목요일과 무엇이 같고 무엇이 다른가

| | 1주차 목요일 | 2주차 목요일 |
|---|---|---|
| 거리 | BFS 이동 횟수 | Dijkstra 에너지(`route_cost`) |
| 그래프 | 트리(경로 유일) | 사이클(보물 사이 최적 경로가 제각각) |
| 예산 | 대체로 넉넉함 | **빠듯함**: 단독으로는 이득인 보물도 버려야 최적 |
| 규모 | 보물 ≤ 12, 순서 DFS도 통과 | 보물 ≤ 15, 에너지도 넉넉한 `grand_tour`: **순서 DFS는 약 20초, DP 필요** |
| 시간 제한 | 2초 | 5초 |

재사용: 1주차의 상태 `(방문 집합, 마지막 보물)`과 전이는 그대로 씁니다. 거리표만 Dijkstra로 바꿉니다.
새로 필요한 것: (1) 거리표를 **출발점 k+1개 × Dijkstra 1번씩**으로 만들기(쌍마다 따로 부르면 k²번), (2) 예산을 넘어 E로 돌아갈 수 없는 상태를 **확장하지 않기**.

## 2. 목적함수 (1주차와 동일)

```
최대화   Σ(가치) − energy(계획)      제약: energy(계획) ≤ obs.energy
energy(계획) = c(S,t1) + 1 + c(t1,t2) + 1 + … + c(tk,E)
```

수집 1 에너지는 **보물마다** 더합니다. 계획이 보물 위를 지나가도 계획에 없으면 줍지 않습니다(`should_collect`가 막음).

## 3. 제공 코드

- `policy_helpers.dijkstra_path`(화요일 TODO의 참고 구현), `route_cost`, `route_to`(목표가 E가 아니면 E를 지나지 않음)
- orchestration이 계획을 따라 이동합니다. `plan_targets`는 첫 턴에 한 번 호출됩니다.

## 4. 맵

| 맵 | 보물 | 무엇을 시험하나 | 최적 점수 |
|---|---:|---|---:|
| `pair_or_prize.json` | 4 | 짝 대 단일 고가 | 163 |
| `budget_tradeoff.json` | 4 | 예산과 지형 | 174 |
| `terrain_bundle.json` | 4 | 지형 묶음 | 171 |
| `cyclic_order.json` | 5 | 사이클 방문 순서, **E가 경로 위** | 199 |
| `graph_challenge.json` | 6 | 종합 | 225 |
| `tight_budget.json` | 7 | 7개 중 3개만: 단독 이득 보물을 버려야 함 | 141 |
| `low_value_bait.json` | 9 | 출구 길목의 저가 미끼 4개 | 226 |
| `grand_tour.json` | 15 | 규모: 12개 수집, DP 필요 | 398 |

**비공개 스트레스 평가(확장성 항목):** 같은 생성 방식의 미공개 맵 2개(보물 16–18개, 격자 ≤ 15×35)에서 10초 안에 계획하는지 확인합니다.
전체 `2^k × k` 표를 모두 도는 DP는 18개에서 느려집니다. 예산 안에서 도달한 상태만 저장하세요.

## 5. 테스트

- `test_student_todo.py`: 작은 사이클 예시(전부 수집 / 예산 부족 시 9짜리를 **밟고 지나가며** 버리기), 8개 맵 최적 점수, 맵당 5초 제한. **starter에서는 실패가 정상**입니다.

## 6. 제출물과 채점(100점)

제출물: `student_policy.py`, 설계 노트, **Ablation 표**.

Ablation이란 같은 맵·같은 예산에서 **전체 방법과 한 요소를 뺀 방법을 비교**하는 것입니다. 최소 다음 4행을 8개 맵에 대해 채우세요.

| 방법 | 맵별 점수 | 계획 시간 |
|---|---|---|
| 바로 탈출 | | |
| 단일 우회 탐욕(화요일 규칙) | | |
| 최근접 우선 탐욕 | | |
| 전역 최적화(여러분의 방법) | | |
| (선택) 예산 가지치기를 끈 DP | | |

| 항목 | 점수 |
|---|---:|
| 정확한 최적화 설계·구현 | 30 |
| 8개 맵 최적 점수 | 20 |
| 시간 제한(공개 5초) | 10 |
| Ablation 표와 해석 | 20 |
| 비공개 스트레스 맵 확장성(10초) | 10 |
| 설계 노트(복잡도, 가지치기가 정답을 바꾸지 않는 이유) | 10 |

## 7. 3시간 운영안

| 시간 | 활동 |
|---|---|
| 0–20분 | 1주차 목요일 코드 재사용 계획, 사이클 예시 손 계산 |
| 20–70분 | Dijkstra 거리표 + DP로 5개 기존 맵 정답 |
| 70–80분 | 휴식 |
| 80–130분 | `tight_budget`, `low_value_bait`, `grand_tour` 통과(가지치기) |
| 130–165분 | Ablation 표 |
| 165–180분 | 설계 노트, 제출 점검 |

```powershell
python -m treasure_explorer --map maps/pair_or_prize.json --agent agent.py --view
Get-ChildItem maps/*.json | ForEach-Object { python -m treasure_explorer --map $_.FullName --agent agent.py }
python -m unittest discover -s tests -v
```

허용: 부분집합 DP, 정확 탐색, branch-and-bound, 정당화한 beam search(비교용). 금지: 하드코딩, 외부 패키지, 파일·네트워크·subprocess·리플렉션.
