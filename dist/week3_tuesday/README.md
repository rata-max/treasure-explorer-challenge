# Week 3 Tuesday — Three-Hour Integrated Hidden Final

한국어 공통 안내: `STUDENT_GUIDE_KO.md`

목요일을 발표에 사용하기 위해 화요일 3시간 안에 구현·테스트·제출을
완료하는 통합형 최종 과제입니다. 부분 관측 탐색의 구현은 고정 `agent.py`에
제공되고, 학생은 hidden value와 안전한 추가 탐색에 관한 두 규칙만 설계합니다.

## Start here

1. `STUDENT_GUIDE_KO.md`에서 제공 기능과 TODO 경계를 읽습니다.
2. 공개 맵 `robustness_practice.json`을 viewer로 한 번 실행합니다.
3. `student_policy.py`의 `should_collect`를 구현합니다.
4. `should_continue_exploring`을 구현하고 안전 여유를 조정합니다.
5. 테스트와 공개 맵 점수를 확인한 뒤 `student_policy.py`만 제출합니다.

## 정확한 수정 범위

- **수정·제출:** `student_policy.py`의 두 TODO와 학생 설정/보조 함수
- **수정 금지:** `agent.py`, `policy_helpers.py`, 엔진, 맵, 테스트, viewer
- 평가는 모든 고정 파일을 깨끗한 공식 사본으로 교체한 뒤 수행합니다.

## 3시간 완주를 위해 제공되는 핵심 기능

- 실행별 상태 생성과 `COLLECT` 전후 상태 유지
- 누적 관측 및 방문 위치 기록
- `?`와 알려진 통행 가능 칸 구분
- frontier 생성과 최저 비용 후보 선택
- 알려진 영역의 Dijkstra 경로 계산
- 관측이 갱신될 때마다 온라인 재계획
- 탐색 중 출구를 경유하지 않도록 하는 보호 장치
- 출구 발견 전 자동 탐색과 출구까지의 정확한 복귀 비용 제공

## 학생 TODO

1. `should_collect`: 보물 가치, 수집 비용 1, 출구 비용, 안전 여유를 비교
2. `should_continue_exploring`: frontier 왕복 비용과 남은 에너지를 비교

frontier 알고리즘 자체는 이 최종 과제의 필수 구현 범위가 아닙니다.

## 화요일 180분 운영안

| 시간 | 활동 |
|---|---|
| 0–20분 | fog, frontier, hidden value, 고정 코드 시연 |
| 20–35분 | starter 실행 및 테스트 확인 |
| 35–70분 | TODO 1 `should_collect` 구현 |
| 70–80분 | 휴식 |
| 80–125분 | TODO 2 `should_continue_exploring` 구현 |
| 125–155분 | 공개 맵 테스트와 threshold 조정 |
| 155–175분 | 결과 기록, 판단식 설명, 제출 점검 |
| 175–180분 | 제출 buffer |

목요일에는 새 코드 활동 없이 화요일에 완성한 정책과 결과를 발표합니다.

## 공개·비공개 평가

- 공개 연습: `maps/robustness_practice.json` 한 개. 이 JSON은 로컬 실행에
  필요한 ground truth이므로 파일을 열면 전체 grid와 실제 value가 보입니다.
- 공개 맵을 실행할 때 agent가 받는 `Observation`은 별개입니다.
  `visibility: local`이 지형을 `?`로, `hidden_values: true`가 T 도착 전
  value를 `None`으로 가립니다.
- 비공개 평가: hidden-value 맵과 추가 private seed
- 실제 Hidden 평가는 map 파일 자체를 학생에게 배포하지 않습니다.
- 공개·비공개 모두 동일한 `student_policy.py`를 수정 없이 실행
- 맵 이름, 좌표, 크기, 모양, seed를 이용한 식별 또는 하드코딩 금지

```powershell
python -m treasure_explorer --map maps/robustness_practice.json --agent agent.py --view
python -m treasure_explorer --map maps/robustness_practice.json --agent agent.py
python -m unittest discover -s tests -v
```
