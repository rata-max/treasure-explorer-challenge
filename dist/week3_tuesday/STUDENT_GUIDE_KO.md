# 학생 안내서: Week 3 화요일 3시간 통합형 Hidden Final

## 이번 과제의 핵심

목요일에는 발표를 진행하므로 화요일 3시간 안에 구현·테스트·제출을 모두
끝냅니다. 부분 관측 탐색기는 완성된 코드로 제공하며, 학생은 탐색기를
고치는 대신 다음 두 질문에 답하는 일반 규칙을 만듭니다.

1. 지금 만난 보물을 수집할 것인가?
2. 출구를 발견한 뒤에도 한 구역을 더 탐색할 것인가?

## 먼저 구분하세요: 파일과 Observation은 다릅니다

`robustness_practice.json`은 공개 디버깅 파일입니다. 로컬 엔진이 정답을
가지고 실행해야 하므로 JSON 원본에는 전체 지형과 실제 treasure value가
들어 있습니다. 학생이 파일을 직접 열면 그 내용을 모두 볼 수 있습니다.

하지만 agent 함수에 전달되는 `Observation`은 다음처럼 마스킹됩니다.

- 보지 않은 지형: `?`
- 아직 도착하지 않은 Treasure의 value: `None`
- 아직 발견하지 않은 Exit: `None`

따라서 공개 practice는 "파일 자체가 비밀"인 맵이 아니라, agent 관점의
부분 관측과 hidden-value API를 연습하는 맵입니다. 진짜 Hidden 평가는 map
파일을 학생에게 배포하지 않고 같은 `student_policy.py`를 실행합니다.

## 수정 범위

| 파일/폴더 | 수정 여부 | 역할 |
|---|---|---|
| `student_policy.py` | **수정·제출** | 두 판단 규칙과 학생용 상수/보조 함수 |
| `agent.py` | **수정 금지** | viewer 연결, 상태, frontier, Dijkstra, 재계획 |
| `policy_helpers.py` | **수정 금지** | 알려진 영역의 경로·frontier 보조 함수 |
| `treasure_explorer/` | 수정 금지 | 엔진, 모델, runner, viewer |
| `maps/`, `tests/` | 수정 금지 | 공개 연습 맵과 계약 검사 |

실행할 때는 `--agent agent.py`를 사용하지만, 제출 파일은
`student_policy.py` 하나뿐입니다.

## 고정 코드가 처리하는 것

- `choose_action`은 매 턴 다시 호출됩니다.
- 실행 중 관측과 방문 상태가 유지되고 새 맵에서만 초기화됩니다.
- 알려진 통행 가능 칸과 `?`를 구분합니다.
- 이동 가능한 frontier를 만들고 가장 저렴한 후보를 선택합니다.
- 알려진 영역에서는 Dijkstra로 최소 에너지 경로를 계산합니다.
- 새 칸이 보일 때마다 현재 관측으로 다시 계획합니다.
- 탐색 경로가 출구를 가로질러 실행이 조기 종료되지 않게 합니다.
- 출구가 보이기 전에는 자동으로 frontier를 탐색합니다.
- 출구가 보이면 학생 TODO에 정확한 탐색 비용과 복귀 비용을 전달합니다.

## TODO 1: 보물을 수집할 것인가

`should_collect(obs, treasure, exit_cost, state)`를 구현합니다.

- `treasure.value`: 현재 칸에서 공개된 보물 가치
- `exit_cost`: 현재 위치에서 출구까지 알려진 최소 에너지. 출구가 아직
  보이지 않으면 `None`
- `state["observed_values"]`: 이번 실행에서 지금까지 확인한 가치 목록
- 수집 자체가 에너지 1을 사용한다는 점을 반드시 포함

권장 판단식의 형태는 다음과 같습니다.

```python
필요_에너지 = 1 + exit_cost + safety_margin
가치_조건 = treasure.value가 내가 정한 기준 이상
return 에너지가_충분함 and 가치_조건
```

## TODO 2: 더 탐색할 것인가

`should_continue_exploring(...)`을 구현합니다. 이 함수는 출구를 발견한
뒤에만 호출됩니다.

- `cost_to_frontier`: 현재 위치에서 후보 frontier까지의 비용
- `cost_frontier_to_exit`: 후보에서 출구까지 알려진 복귀 비용
- `obs.energy`: 현재 남은 에너지

최소 안전 조건은 다음 구조입니다.

```python
필요_에너지 = cost_to_frontier + cost_frontier_to_exit + safety_margin
return obs.energy >= 필요_에너지
```

이 조건을 그대로 쓸 수도 있지만, 좋은 점수를 위해 관측한 보물 가치와
위험 여유를 이용해 탐색 중단 시점을 조절할 수 있습니다.

## `COLLECT`에서 흔히 생기는 오해

1. `T` 위로 이동해도 아직 수집되지 않습니다.
2. 다음 호출에서 `should_collect(...)`가 `True`이면 고정 코드가
   `COLLECT`를 반환합니다.
3. 위치는 그대로이고 에너지 1이 감소합니다.
4. 다음 관측에서 `TreasureInfo.collected=True`가 됩니다.
5. 격자 문자는 계속 `T`지만 이전 상태는 초기화되지 않습니다.

따라서 `grid[row][col] == "T"`로 수집 여부를 판단하면 안 됩니다.

## 알고리즘과 라이브러리 규칙

- 학생 TODO는 **observation-only rule-based 정책**이어야 합니다.
- 고정 코드가 frontier와 Dijkstra를 수행하므로 별도의 탐색 알고리즘
  구현은 필수가 아닙니다.
- Python 3.11+ 표준 라이브러리만 허용합니다.
- PyTorch, NumPy, 학습·사전학습 모델, 외부 패키지는 금지합니다.
- 파일·네트워크·subprocess·reflection·side channel 접근은 금지합니다.
- 맵 이름, 좌표, 크기, 모양, seed, 외운 경로에 따른 분기는 금지합니다.
- 서로 다른 평가 실행 사이에 상태나 정보를 공유하면 안 됩니다.
- 공개 JSON을 사람이 읽는 것은 디버깅상 가능하지만, 그 좌표·value·layout을
  외워 policy에 넣으면 private map에 일반화되지 않으며 평가 규칙 위반입니다.

## 실행 순서

1. 기본 정책으로 viewer를 실행해 출구 발견 전후 행동을 관찰합니다.
2. `should_collect` 하나만 구현하고 테스트합니다.
3. `should_continue_exploring`을 구현합니다.
4. 전체 단위 테스트를 통과시킵니다.
5. 공개 맵에서 탈출, invalid action 0, 점수를 함께 확인합니다.

## 180분 일정

| 시간 | 해야 할 일 | 완료 표시 |
|---|---|---|
| 0–20분 | 강의 시연: fog, frontier, hidden value | 개념 확인 |
| 20–35분 | starter와 test 실행 | 기본 탈출 확인 |
| 35–70분 | TODO 1 구현 | 수집 판단 완성 |
| 70–80분 | 휴식 |  |
| 80–125분 | TODO 2 구현 | 탐색 중단 판단 완성 |
| 125–155분 | 공개 맵 반복 실행·조정 | invalid 0 확인 |
| 155–175분 | 결과와 판단식 정리 | 발표 자료용 기록 |
| 175–180분 | `student_policy.py` 제출 | 제출 완료 |

목요일에는 코드를 더 수정하지 않고 화요일에 제출한 정책의 설계와 결과를
발표합니다.

```powershell
python -m treasure_explorer --map maps/robustness_practice.json --agent agent.py --view --no-clear
python -m unittest discover -s tests -v
```

## 제출 전 체크리스트

- 수정한 파일이 `student_policy.py` 하나인가?
- 출구까지의 비용과 수집 비용 1을 예약했는가?
- `?`를 통행 가능한 바닥으로 가정하지 않았는가?
- 공개 맵의 이름·좌표·크기에 의존하지 않는가?
- 기본 테스트가 모두 통과하는가?
- 처음 보는 맵에서도 같은 규칙을 설명할 수 있는가?
