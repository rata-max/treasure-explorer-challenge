// Edit this file and click "Commit changes". GitHub Pages updates automatically.
window.SITE_CONTENT = {
  semester: "Problem Solving Techniques · Fall 2026",
  badge: "3-HOUR LABS",
  title: "Explore.",
  subtitle: "Collect. Return.",
  description: "Five stages over three weeks, each harder than the last: write BFS, then subset search, then Dijkstra, then budgeted optimisation, then an exploration strategy under fog. Every energy unit you keep is a point, and no exit means no score.",
  labHours: "3H", initialEnergy: "MAP", submission: "student_policy.py",
  pythonVersion: "Python 3.11+",
  command: "python -m treasure_explorer --map maps/warmup.json --agent agent.py --view",
  scoreFormula: "50 EXIT BONUS + TREASURE + ENERGY LEFT - 5 INVALID",
  noExitRule: "NO EXIT, NO SCORE",
  missionLabel: "01 / MISSION",
  missionTitle: "One policy file. Every map in the stage.",
  missionDescription: "Read the current Observation, decide, and let the fixed agent take one action. A treasure is worth its value minus the extra energy it costs.",
  process: [["01","OBSERVE","Map · Energy"],["02","ESTIMATE","Value − extra energy"],["03","PLAN","Target · Route"],["04","ACT","One action"]],
  rules: [
    {number:"RULE 01",title:"Information changes by stage",text:"Weeks 1–2 maps are fully public. Week 3 hides terrain, the exit and treasure values until observed."},
    {number:"RULE 02",title:"Return first",text:"Treasure counts only after the bot reaches the exit. Entering the exit ends the run, so routes to treasure must not cross it."},
    {number:"RULE 03",title:"Energy is score",text:"Normal 1 · Mud 4 · Water 7 · Collect 1. Energy left at the exit is added to the score."}
  ],
  schedule: [
    ["00:00","Inspect","Read the README, run the tests (TODO tests fail on the starter)."],
    ["00:20","Implement","TODO 1 until its tests pass."],
    ["01:20","Break","10 minutes."],
    ["01:30","Decide","Remaining TODOs: profit and energy-safety rules."],
    ["02:10","Measure","Run every map, compare with the reference scores."],
    ["02:40","Report","Design note and submission check."]
  ],
  rubric: [
    ["25–30","Algorithm","The stage's own algorithm: BFS, subset search, Dijkstra, budgeted DP, exploration strategy"],
    ["20–25","Score","Required level, exact optimum, or private evaluation, depending on the stage"],
    ["10–20","Safety","Exit on every map, 0 invalid actions, planning time limit"],
    ["15–20","Analysis","Greedy counterexample, BFS vs Dijkstra table, ablation, or seed experiments"],
    ["10–15","Design note","Complexity, decisions and their limits. Exact rubric: each stage README"]
  ],
  submissionRules: [
    "Run with --agent agent.py, but edit and submit only student_policy.py (plus the design note).",
    "Do not modify agent.py, policy_helpers.py, the engine, maps, tests, or configuration files.",
    "The agent must not access files, networks, subprocesses, or external packages."
  ],
  integrityRules: [
    "Do not copy or share another student's agent code.",
    "Do not publish solution code in a public repository before grading ends.",
    "Do not identify hidden maps or seeds through hardcoding or side channels.",
    "Declare external code, references, and permitted AI assistance in the report."
  ]
};

/* Five sequential releases. TA: unlock only the next item. Keep unreleased ZIPs off the public branch. */
window.SITE_CONTENT.stages = [
{number:"01",week:"WEEK 1",day:"TUESDAY",title:"TREE PLANNING FOUNDATIONS ★★",unlocked:true,tagline:"Write BFS yourself, then decide which treasure detours pay off.",focus:"BFS · Path recovery · Profit = value − extra energy",repositoryUrl:"https://github.com/rata-max/te-releases/releases/download/week1-tue/week1_tuesday.zip",objectives:["Implement your own bfs_path ([] when already there, None when unreachable, parent-dictionary recovery). A reference BFS keeps the starter running, but a submission that runs only on the reference BFS (USE_MY_BFS = False) loses 20 points.","Implement should_collect: value > 1 and the exit still affordable after the 1-energy COLLECT.","Implement select_target with the single-detour rule gain = value − (d(here,t) + 1 + d(t,E) − d(here,E)).","Pass tests/test_student_todo.py and exit all four maps with 0 invalid actions. Optional bonus: visit order."],deliverables:["student_policy.py with USE_MY_BFS = True","Design note: BFS O(V+E), score table, why two maps stay below the optimum"],evaluation:{label:"TUESDAY EVALUATION",title:"Your own BFS, safe exits, profitable detours.",text:"Reference-BFS-only submissions lose 20 points. Reference scores (optimum 67 / 90 / 78 / 84) are in the README."}},
{number:"02",week:"WEEK 1",day:"THURSDAY",title:"GLOBAL TREE OPTIMIZATION ★★★",unlocked:true,tagline:"Eight tree maps up to 12 treasures: choose the subset and the order.",focus:"Subset DP · Pruned search · 2 s limit",repositoryUrl:"https://github.com/rata-max/te-releases/releases/download/week1-thu/week1_thursday.zip",objectives:["Implement plan_targets with an exact method: budget-pruned order search or subset DP over (visited set, last treasure).","Reach the exact optimum on all eight maps; the tests know the optimal scores.","Plan within 2 seconds per map; 12 treasures rule out plain permutations.","Explain one greedy counterexample (nearest-first, highest-value or ratio) with real map numbers."],deliverables:["student_policy.py","Design note: state, transition, O(2^k·k²), greedy counterexample, score and time table"],evaluation:{label:"THURSDAY EVALUATION",title:"Exact optimum on eight public trees.",text:"A worked DP table for a shared-branch example is in the README."}},
{number:"03",week:"WEEK 2",day:"TUESDAY",title:"WEIGHTED GRAPH ROUTES ★★★",unlocked:true,tagline:"Write Dijkstra yourself: fewer steps is not less energy.",focus:"Dijkstra · Priority queue · Exit avoidance",repositoryUrl:"https://github.com/rata-max/te-releases/releases/download/week2-tue/week2_tuesday.zip",objectives:["Implement dijkstra_path with heapq, stale-entry skipping and parent recovery: ([],0) when there, (None,None) when unreachable.","Reuse the single-detour rule with energy costs from route_cost, which never crosses the exit.","Meet the required score on seven maps, including a map where hop-count planning runs out of energy and one where the exit blocks the way.","Compare BFS and Dijkstra decisions on every map."],deliverables:["student_policy.py","Design note: Dijkstra complexity, BFS vs Dijkstra table"],evaluation:{label:"PRACTICE EVALUATION",title:"Your own Dijkstra on seven weighted maps.",text:"Hop-count BFS scores 0 on energy_illusion.json."}},
{number:"04",week:"WEEK 2",day:"THURSDAY",title:"PRIZE-COLLECTING GRAPH ★★★★",unlocked:true,tagline:"Tight budgets, low-value bait and a 15-treasure grand tour on cyclic weighted graphs.",focus:"Budgeted subset DP · Pruning · 5 s limit",repositoryUrl:"https://github.com/rata-max/te-releases/releases/download/week2-thu/week2_thursday.zip",objectives:["Implement plan_targets on Dijkstra costs (one Dijkstra per source, not per pair).","Reach the exact optimum on eight maps within 5 seconds each; order enumeration takes about 20 s on grand_tour.json.","Only expand states that can still reach the exit within budget; unreleased 16–18-treasure maps check scalability.","Build an ablation table: direct exit, single-detour greedy, nearest-first, your method."],deliverables:["student_policy.py","Design note","Ablation table"],evaluation:{label:"CHALLENGE EVALUATION",title:"Exact optimum under tight budgets and time limits.",text:"Two unreleased stress maps test planning time up to 18 treasures."}},
{number:"05",week:"WEEK 3",day:"TUESDAY",title:"HIDDEN FINAL CHALLENGE ★★★★★",unlocked:true,tagline:"Fog, hidden values and an unknown exit: choose where to go and prove it with experiments.",focus:"Online decisions · Expected gain · Experiment design",repositoryUrl:"https://github.com/rata-max/te-releases/releases/download/week3-tue/week3_tuesday.zip",objectives:["Implement should_collect(obs, treasure, exit_cost, state), including the exit_cost is None case.","Implement choose_target(obs, options, state): steer the search before the exit is known and weigh expected gain against extra energy after.","Check option.cost_to + option.cost_to_exit + SAFETY_MARGIN <= energy yourself; nothing else prevents a zero-score run.","Tune on one seed range with evaluate.py and report on another. Minimum bar: mean ≥ 200 and exit ≥ 90 % on seeds 0–29."],deliverables:["student_policy.py","Design note with experiment table","5-minute Thursday presentation"],evaluation:{label:"FINAL EVALUATION",title:"Unpublished seeds of the public generator.",text:"Thursday is presentation only — no new code. Ranked by mean score, exit rate, invalid actions and the quality of the experiments."}}
];

window.SITE_CONTENT.stageRules = [
["Four public tree maps: warmup, two branches, greedy trap, energy budget.","Every move costs 1 energy and COLLECT costs 1. Energy left is score.","You write bfs_path; reference_bfs_path is only a fallback so the starter runs. Submitting with the reference BFS only costs 20 points.","Entering the exit ends the run immediately; a route to a treasure must treat E as a wall.","tests/test_student_todo.py fails on the starter by design and passes when your TODOs are correct.","Submit student_policy.py unchanged across all four maps; do not modify agent.py."],
["Eight public tree maps with up to 12 treasures.","Branches can share edges; evaluate the whole route start -> treasures -> exit.","The exact optimum is required on every map; plan_targets must finish within 2 s.","Exact enumeration with budget pruning, subset DP and branch-and-bound are allowed; heuristics only for comparison.","Submit student_policy.py unchanged across all eight maps; do not modify agent.py."],
["Seven public weighted maps with mud (4) and water (7).","You write dijkstra_path; bfs_path is provided only for comparison.","Terrain cost is charged when a cell is entered; the fewest-step path may not be the lowest-energy path.","The exit ends the run immediately and may not be used as an intermediate waypoint.","Submit student_policy.py unchanged across all seven maps; do not modify agent.py."],
["Eight public cyclic weighted graphs with up to 15 treasures.","Budgets are tight: the optimum may skip treasures that look profitable alone.","The exact optimum is required; plan_targets must finish within 5 s per map.","Two unreleased maps with 16–18 treasures check planning time (10 s).","Submit student_policy.py unchanged across all maps; map-name and layout hardcoding are prohibited."],
["Three-hour final. Thursday is presentation only — no new code after this lab.","Five public practice maps plus a public generator; private evaluation uses unpublished seeds of the same generator and hand-made maps with the same rules.","The fixed agent.py builds frontier and treasure options and moves by Dijkstra; you choose the target and the collection rule.","Unobserved cells are ?; they are NOT assumed passable. The exit is None until revealed.","The fixed code does not guarantee an exit: check the energy needed to get back yourself.","Hardcoded coordinates, map fingerprints, map names, and seed detection are prohibited; no state may be shared between runs."]
];

/* Commands shown on the homepage and assignment pages. */
window.SITE_CONTENT.stageCommands = [
  "python -m treasure_explorer --map maps/warmup.json --agent agent.py --view",
  "python -m treasure_explorer --map maps/shared_branch.json --agent agent.py --view",
  "python -m treasure_explorer --map maps/terrain_choice.json --agent agent.py --view",
  "python -m treasure_explorer --map maps/pair_or_prize.json --agent agent.py --view",
  "python -m treasure_explorer --map maps/robustness_practice.json --agent agent.py --view"
];

window.SITE_CONTENT.batchCommands = {
  powershell: "Get-ChildItem maps/*.json | ForEach-Object { python -m treasure_explorer --map $_.FullName --agent agent.py }",
  bash: "for map in maps/*.json; do python -m treasure_explorer --map \"$map\" --agent agent.py; done",
  tests: "python -m unittest discover -s tests -v"
};

/* ============================================================
   KOREAN TRANSLATIONS  (한국어 번역)
   Edit window.SITE_CONTENT_KO to update Korean text only.
   ============================================================ */
window.SITE_CONTENT_KO = {
  semester: "문제해결기법 · 2026년 가을학기",
  badge: "3시간 실습",
  title: "탐험하라.",
  subtitle: "수집하라. 귀환하라.",
  description: "3주 동안 다섯 단계, 갈수록 어려워집니다. BFS 직접 구현 → 부분집합 탐색 → Dijkstra 직접 구현 → 예산 제약 최적화 → 안개 속 탐색 전략. 남긴 에너지 1이 1점이고, 출구에 도달하지 못하면 0점입니다.",
  labHours: "3H", initialEnergy: "MAP", submission: "student_policy.py",
  pythonVersion: "Python 3.11+",
  command: "python -m treasure_explorer --map maps/warmup.json --agent agent.py --view",
  scoreFormula: "50 출구 보너스 + 보물 가치 + 남은 에너지 - 5 × 무효 행동",
  noExitRule: "출구 미도달 시 점수 없음",
  missionLabel: "01 / 임무",
  missionTitle: "정책 파일 하나. 단계의 모든 맵.",
  missionDescription: "현재 Observation을 읽고 판단하면, 고정 에이전트가 행동 하나를 실행합니다. 보물의 순이익은 가치에서 추가로 쓴 에너지를 뺀 값입니다.",
  process: [["01","관측","맵 · 에너지"],["02","추정","가치 − 추가 에너지"],["03","계획","목표 · 경로"],["04","행동","행동 하나"]],
  rules: [
    {number:"규칙 01",title:"단계마다 정보가 달라집니다",text:"1–2주차 맵은 모두 공개됩니다. 3주차는 지형·출구·보물 가치를 관측하기 전까지 가립니다."},
    {number:"규칙 02",title:"귀환이 먼저입니다",text:"출구에 도달해야 보물 점수가 인정됩니다. 출구에 들어가면 즉시 끝나므로 보물로 가는 경로는 출구를 지나면 안 됩니다."},
    {number:"규칙 03",title:"에너지가 점수입니다",text:"일반 1 · 진흙 4 · 물 7 · 수집 1. 출구에서 남은 에너지가 점수에 더해집니다."}
  ],
  schedule: [
    ["00:00","점검","README를 읽고 테스트 실행(TODO 테스트는 starter에서 실패가 정상)."],
    ["00:20","구현","TODO 1을 테스트가 통과할 때까지."],
    ["01:20","휴식","10분."],
    ["01:30","판단","나머지 TODO: 이익 규칙과 에너지 안전 규칙."],
    ["02:10","측정","모든 맵 실행, 기준 점수와 비교."],
    ["02:40","보고","설계 노트 작성과 제출 점검."]
  ],
  rubric: [
    ["25–30","알고리즘","단계 고유 알고리즘: BFS, 부분집합 탐색, Dijkstra, 예산 DP, 탐색 전략"],
    ["20–25","점수","단계에 따라 필수 수준, 정확한 최적, 비공개 평가"],
    ["10–20","안전","모든 맵 탈출, 무효 행동 0, 계획 시간 제한"],
    ["15–20","분석","탐욕 반례, BFS 대 Dijkstra 표, ablation, 시드 실험"],
    ["10–15","설계 노트","복잡도, 판단과 한계. 정확한 채점표는 각 단계 README"]
  ],
  submissionRules: [
    "실행은 --agent agent.py로 하지만, 수정·제출하는 파일은 student_policy.py(와 설계 노트)뿐입니다.",
    "agent.py, policy_helpers.py, 엔진, 맵, 테스트, 설정 파일은 수정하지 마세요.",
    "에이전트는 파일, 네트워크, 서브프로세스, 외부 패키지에 접근해서는 안 됩니다."
  ],
  integrityRules: [
    "다른 학생의 에이전트 코드를 복사하거나 공유하지 마세요.",
    "채점이 끝나기 전에 솔루션 코드를 공개 저장소에 게시하지 마세요.",
    "하드코딩이나 사이드 채널로 숨겨진 맵이나 시드를 식별하지 마세요.",
    "보고서에 외부 코드, 참고 자료, 허용된 AI 사용을 명시하세요."
  ]
};

window.SITE_CONTENT_KO.stages = [
  {number:"01",week:"1주차",day:"화요일",title:"트리 계획 기초 ★★",unlocked:true,tagline:"BFS를 직접 구현하고, 어떤 보물 우회가 이득인지 판단하세요.",focus:"BFS · 경로 복원 · 순이익 = 가치 − 추가 에너지",repositoryUrl:"https://github.com/rata-max/te-releases/releases/download/week1-tue/week1_tuesday.zip",objectives:["bfs_path 직접 구현(도착이면 [], 도달 불가면 None, parent 딕셔너리로 경로 복원). 참고 BFS로 starter는 바로 실행되지만, 참고 BFS로만 실행되는 제출(USE_MY_BFS = False)은 20점 감점입니다.","should_collect 구현: 가치 > 1이고 수집(1) 후에도 출구까지 갈 에너지가 남을 때.","select_target 구현: 단일 우회 규칙 gain = 가치 − (d(현재,t) + 1 + d(t,E) − d(현재,E)).","tests/test_student_todo.py 통과, 4개 맵 무효 행동 0으로 탈출. 선택 보너스: 방문 순서."],deliverables:["student_policy.py (USE_MY_BFS = True)","설계 노트: BFS O(V+E), 점수표, 두 맵이 최적에 못 미치는 이유"],evaluation:{label:"화요일 평가",title:"직접 만든 BFS, 안전한 탈출, 이득인 우회.",text:"참고 BFS로만 실행되는 제출은 20점 감점입니다. 기준 점수(최적 67 / 90 / 78 / 84)는 README에 있습니다."}},
  {number:"02",week:"1주차",day:"목요일",title:"전역 트리 최적화 ★★★",unlocked:true,tagline:"보물 최대 12개의 트리 맵 8개: 부분집합과 순서를 고르세요.",focus:"부분집합 DP · 가지치기 탐색 · 2초 제한",repositoryUrl:"https://github.com/rata-max/te-releases/releases/download/week1-thu/week1_thursday.zip",objectives:["plan_targets를 정확한 방법으로 구현: 예산 가지치기 순서 탐색 또는 (방문 집합, 마지막 보물) 부분집합 DP.","8개 맵 모두 정확한 최적 점수(테스트가 최적 점수를 확인).","맵당 2초 안에 계획: 보물 12개에서는 순열 전수조사가 불가능.","탐욕 반례(최근접·최고가·비율) 하나를 실제 맵 숫자로 설명."],deliverables:["student_policy.py","설계 노트: 상태·전이·O(2^k·k²)·탐욕 반례·점수와 시간표"],evaluation:{label:"목요일 평가",title:"공개 트리 8개에서 정확한 최적.",text:"공유 분기 예시의 DP 표가 README에 있습니다."}},
  {number:"03",week:"2주차",day:"화요일",title:"가중 그래프 경로 ★★★",unlocked:true,tagline:"Dijkstra를 직접 구현하세요: 적게 걷는 길이 적게 드는 길은 아닙니다.",focus:"Dijkstra · 우선순위 큐 · 출구 경유 금지",repositoryUrl:"https://github.com/rata-max/te-releases/releases/download/week2-tue/week2_tuesday.zip",objectives:["heapq, stale 항목 건너뛰기, parent 복원으로 dijkstra_path 구현: 도착이면 ([],0), 도달 불가면 (None,None).","출구를 지나지 않는 route_cost의 에너지 비용으로 단일 우회 규칙 재사용.","7개 맵 필수 점수 달성: 이동 횟수로 판단하면 에너지가 바닥나는 맵, 출구가 길을 막는 맵 포함.","모든 맵에서 BFS와 Dijkstra 판단 비교."],deliverables:["student_policy.py","설계 노트: Dijkstra 복잡도, BFS 대 Dijkstra 표"],evaluation:{label:"실습 평가",title:"직접 만든 Dijkstra로 가중 맵 7개.",text:"이동 횟수 BFS는 energy_illusion.json에서 0점입니다."}},
  {number:"04",week:"2주차",day:"목요일",title:"상금 수집 그래프 ★★★★",unlocked:true,tagline:"사이클 가중 그래프에서 빠듯한 예산, 저가 미끼, 보물 15개 그랜드 투어.",focus:"예산 제약 부분집합 DP · 가지치기 · 5초 제한",repositoryUrl:"https://github.com/rata-max/te-releases/releases/download/week2-thu/week2_thursday.zip",objectives:["Dijkstra 비용으로 plan_targets 구현(쌍마다가 아니라 출발점마다 Dijkstra 한 번).","8개 맵 정확한 최적을 맵당 5초 안에: grand_tour.json에서 순서 탐색은 약 20초.","예산 안에 출구로 돌아갈 수 있는 상태만 확장. 미공개 16–18개 보물 맵으로 확장성 확인.","Ablation 표: 바로 탈출, 단일 우회 탐욕, 최근접 우선, 여러분의 방법."],deliverables:["student_policy.py","설계 노트","Ablation 표"],evaluation:{label:"도전 평가",title:"빠듯한 예산과 시간 제한에서 정확한 최적.",text:"미공개 스트레스 맵 2개가 보물 18개까지의 계획 시간을 확인합니다."}},
  {number:"05",week:"3주차",day:"화요일",title:"숨겨진 최종 도전 ★★★★★",unlocked:true,tagline:"안개·숨은 가치·모르는 출구: 어디로 갈지 고르고 실험으로 증명하세요.",focus:"온라인 판단 · 기대 이익 · 실험 설계",repositoryUrl:"https://github.com/rata-max/te-releases/releases/download/week3-tue/week3_tuesday.zip",objectives:["should_collect(obs, treasure, exit_cost, state) 구현, exit_cost가 None인 경우 포함.","choose_target(obs, options, state) 구현: 출구 발견 전에는 탐색 방향을, 발견 후에는 기대 이익과 추가 에너지를 비교.","option.cost_to + option.cost_to_exit + SAFETY_MARGIN <= energy를 직접 확인. 다른 안전장치는 없습니다.","evaluate.py로 한 시드 범위에서 조정하고 다른 범위에서 보고. 최소 기준: 시드 0–29 평균 200 이상, 탈출률 90% 이상."],deliverables:["student_policy.py","실험 표가 있는 설계 노트","목요일 5분 발표"],evaluation:{label:"최종 평가",title:"공개 생성기의 미공개 시드로 평가.",text:"목요일은 발표만 진행합니다 — 새 코드 없음. 평균 점수·탈출률·무효 행동과 실험의 질로 평가합니다."}}
];

window.SITE_CONTENT_KO.stageRules = [
  ["공개 트리 맵 4개: warmup, 두 분기, 탐욕 함정, 에너지 예산.","이동은 에너지 1, COLLECT도 1. 남은 에너지가 점수입니다.","bfs_path는 직접 작성합니다. reference_bfs_path는 starter 실행용 대체 함수이며, 이것으로만 실행되는 제출은 20점 감점입니다.","출구에 들어가면 즉시 종료됩니다. 보물로 가는 경로에서는 E를 벽처럼 취급하세요.","tests/test_student_todo.py는 starter에서 실패하도록 만들어져 있고, TODO가 맞으면 통과합니다.","student_policy.py를 4개 맵 전체에서 수정 없이 제출하세요. agent.py는 수정하지 마세요."],
  ["보물 최대 12개의 공개 트리 맵 8개.","분기는 간선을 공유할 수 있으므로 시작 → 보물들 → 출구 전체 경로로 평가하세요.","모든 맵에서 정확한 최적이 필요하며, plan_targets는 2초 안에 끝나야 합니다.","예산 가지치기 완전 탐색, 부분집합 DP, branch-and-bound 허용. 휴리스틱은 비교용으로만.","student_policy.py를 8개 맵 전체에서 수정 없이 제출하세요. agent.py는 수정하지 마세요."],
  ["진흙(4)과 물(7)이 있는 공개 가중 맵 7개.","dijkstra_path는 직접 작성합니다. bfs_path는 비교용으로만 제공됩니다.","셀에 진입할 때 지형 비용이 부과됩니다. 이동 횟수가 가장 적은 경로가 에너지 최소 경로가 아닐 수 있습니다.","출구는 게임을 즉시 종료하며 중간 경유지로 사용할 수 없습니다.","student_policy.py를 7개 맵 전체에서 수정 없이 제출하세요. agent.py는 수정하지 마세요."],
  ["보물 최대 15개의 공개 사이클 가중 그래프 8개.","예산이 빠듯합니다. 최적 계획은 단독으로는 이득인 보물을 버릴 수 있습니다.","정확한 최적이 필요하며, plan_targets는 맵당 5초 안에 끝나야 합니다.","보물 16–18개의 미공개 맵 2개로 계획 시간(10초)을 확인합니다.","동일한 student_policy.py가 모든 맵에서 수정 없이 실행돼야 합니다. 맵 이름과 레이아웃 하드코딩은 금지됩니다."],
  ["3시간 최종 실습입니다. 목요일은 발표만 진행합니다 — 이 실습 이후 새 코드는 없습니다.","공개 연습 맵 5개와 공개 생성기가 제공됩니다. 비공개 평가는 같은 생성기의 미공개 시드와 같은 규칙의 수작업 맵을 사용합니다.","고정 agent.py가 frontier와 보물 옵션을 만들고 Dijkstra로 이동합니다. 목표 선택과 수집 규칙은 여러분이 정합니다.","관측되지 않은 셀은 ?입니다. 통과 가능하다고 가정하지 마세요. 출구는 공개될 때까지 None입니다.","고정 코드는 탈출을 보장하지 않습니다. 돌아올 에너지는 직접 확인하세요.","하드코딩된 좌표, 맵 지문, 맵 이름, 시드 탐지는 금지되며, 실행 사이에 상태를 공유할 수 없습니다."]
];

window.SITE_CONTENT_KO.stageCommands = window.SITE_CONTENT.stageCommands;
window.SITE_CONTENT_KO.batchCommands = window.SITE_CONTENT.batchCommands;
