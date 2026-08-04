// 평소에는 이 파일만 수정하세요. 따옴표 안의 문구를 바꾸고 Commit changes를 누르면 됩니다.
window.SITE_CONTENT = {
  semester: "2026-2 문제해결기법",
  badge: "PS 2026 · WEEK 01",
  title: "Find the treasure.",
  subtitle: "Make it back.",
  description: "보물의 가치는 숨겨져 있고, 지형은 움직일 때 드러납니다. 제한된 에너지 안에서 탐색하고 판단하고, 반드시 출구로 귀환하세요.",
  labHours: "6H",
  initialEnergy: "100",
  submission: "student/agent.py",
  pythonVersion: "Python 3.11+",
  command: "python -m treasure_explorer --map maps/example_easy.json --agent student/agent.py",
  scoreFormula: "Σ TREASURE + ENERGY LEFT - 5 × INVALID",
  noExitRule: "EXIT에 도달하지 못하면 SCORE = 0",
  rules: [
    { number: "RULE 01", title: "움직이면 드러난다", text: "진흙과 물은 인접했을 때 공개되고, 보물 가치는 도착한 뒤에야 알 수 있습니다." },
    { number: "RULE 02", title: "가치보다 귀환", text: "보물을 아무리 많이 모아도 출구에 도달하지 못하면 최종 점수는 0점입니다." },
    { number: "RULE 03", title: "에너지는 유한하다", text: "일반 칸 1, 진흙 4, 물 5. 수집에도 에너지 1이 필요합니다." }
  ],
  schedule: [
    ["00:00", "환경 탐색", "엔진을 실행하고 Observation과 좌표계를 확인합니다."],
    ["00:40", "경로 복원", "BFS로 현재 위치에서 출구까지 실제 행동열을 만듭니다."],
    ["02:10", "가중치 대응", "진흙과 물을 고려하도록 Dijkstra로 확장합니다."],
    ["03:10", "상태 관리", "보물의 미확인·확인·수집 상태를 일관되게 관리합니다."],
    ["04:20", "안전한 선택", "후보를 방문해도 출구로 돌아올 에너지가 있는지 검사합니다."],
    ["05:20", "회귀 테스트", "공개 맵에서 실패 사례를 찾고 전략을 다듬습니다."]
  ],
  rubric: [
    ["20", "안전한 종료", "모든 공개 맵에서 출구 도달"],
    ["20", "경로 탐색", "BFS/Dijkstra와 경로 복원"],
    ["15", "온라인 재계획", "매 턴 최신 관측 반영"],
    ["10", "에너지 검증", "수집 후 복귀 가능성 검사"],
    ["25", "성능·품질", "비공개 점수와 코드 품질"],
    ["10", "설계 메모", "복잡도와 실패 사례 분석"]
  ]
};
