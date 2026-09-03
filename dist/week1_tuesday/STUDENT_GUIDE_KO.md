# 학생 안내서: 엔진이 아니라 정책만 수정하세요

## 수정 범위

| 파일/폴더 | 수정 여부 | 역할 |
|---|---|---|
| `student_policy.py` | **수정·제출** | 학생의 규칙과 탐색 알고리즘 |
| `agent.py` | **수정 금지** | viewer/평가기 연결과 실행별 상태 초기화 |
| `policy_helpers.py` | 일반적으로 수정 금지 | BFS, Dijkstra, frontier 보조 함수 |
| `treasure_explorer/` | 수정 금지 | 엔진, 모델, runner, viewer |
| `maps/`, `tests/` | 수정 금지 | 입력 맵과 계약 검사 |

실행 명령은 계속 `--agent agent.py`를 사용하지만, 학생은
`student_policy.py`만 편집하고 제출합니다.

## `choose_action`은 매 턴 다시 호출됩니다

함수 내부의 지역 변수는 호출이 끝나면 사라집니다. 여러 턴 동안 유지할
`visited`, `parent`, DFS stack, 목표 목록은 `make_state()`가 만든 `state`에
저장하세요. 고정 `agent.py`는 새 맵이 시작될 때만 이 상태를 초기화합니다.

보물 수집은 다음과 같이 진행됩니다.

1. 이동하여 `T`에 도착합니다.
2. 다음 호출에서 `should_collect(...)`가 `True`이면 `COLLECT`를 반환합니다.
3. 위치는 그대로이고 에너지만 1 감소합니다.
4. 다음 관측에서 `TreasureInfo.collected=True`가 됩니다.
5. 이전과 같은 `state`가 전달되므로 저장한 복귀 경로를 계속 사용합니다.

수집 후에도 격자의 문자는 계속 `T`입니다. 따라서 다음 코드는 수집 여부를
판별하지 못합니다.

```python
if obs.grid[row][col] == "T":  # 이미 수집한 뒤에도 True
    ...
```

수집 여부는 반드시 `TreasureInfo.collected`로 확인하세요. T 도착, 수집,
목표 도달을 이유로 `visited`, `parent`, DFS stack 전체를 초기화하면 안 됩니다.

## 알고리즘과 라이브러리

| 단계 | 필수/권장 알고리즘 |
|---|---|
| Week 1 Tuesday | BFS 또는 DFS와 parent 기반 경로 복원 |
| Week 1 Thursday | Tree/subset DP, 완전탐색, branch-and-bound |
| Week 2 Tuesday | Dijkstra 또는 UCS; 조건부 A* 허용 |
| Week 2 Thursday | Dijkstra + subset/order 최적화 |
| Week 3 Tuesday | frontier, 누적 상태, 온라인 재계획 |
| Week 3 Thursday | observation-only 범용 rule-based 정책 |

Python 3.11+ 표준 라이브러리만 사용할 수 있습니다. PyTorch, NumPy, 학습된
모델, 외부 패키지, 파일·네트워크·subprocess 접근은 허용되지 않습니다.

## 디버깅 순서

1. `python -m unittest discover -s tests -v`
2. 한 맵을 `--view --no-clear`로 실행
3. `student_policy.py`의 TODO 하나만 수정
4. 전체 맵 실행
5. 탈출 여부, invalid action, 남은 에너지를 함께 비교
