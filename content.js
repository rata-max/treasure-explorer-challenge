// Edit this file and click "Commit changes". GitHub Pages updates automatically.
window.SITE_CONTENT = {
  semester: "Problem Solving Techniques · Fall 2026",
  badge: "6-HOUR LAB",
  title: "Explore.",
  subtitle: "Collect. Return.",
  description: "Build one generic agent per stage. Run it unchanged across every released map, collect profitable treasure, and always preserve a safe route to the exit.",
  labHours: "6H", initialEnergy: "MAP", submission: "student_policy.py",
  pythonVersion: "Python 3.11+",
  command: "python -m treasure_explorer --map maps/warmup.json --agent agent.py --view",
  scoreFormula: "50 EXIT BONUS + TREASURE + ENERGY LEFT - 5 INVALID",
  noExitRule: "NO EXIT, NO SCORE",
  missionLabel: "01 / MISSION",
  missionTitle: "One agent. Every map in the stage.",
  missionDescription: "Read the current Observation, select one valid Action, and repeat.",
  process: [["01","OBSERVE","Map · Energy"],["02","ESTIMATE","Value · Return cost"],["03","PLAN","Target · Route"],["04","ACT","One action"]],
  rules: [
    {number:"RULE 01",title:"Information changes by stage",text:"Week 1 maps are public. Week 3 reveals only the information included in each Observation."},
    {number:"RULE 02",title:"Return first",text:"Treasure counts only after the bot reaches the exit."},
    {number:"RULE 03",title:"Budget energy",text:"Normal: 1 · Mud: 4 · Water: 7 · Collect: 1"}
  ],
  schedule: [
    ["00:00","Inspect","Run the engine and inspect Observation."],
    ["00:40","Route","Build and recover a path with BFS."],
    ["02:10","Weight","Upgrade to Dijkstra for terrain costs."],
    ["03:10","State","Track unseen, seen, and collected treasure."],
    ["04:20","Safety","Verify energy reserved for the return route."],
    ["05:20","Test","Run public maps and analyze failures."]
  ],
  rubric: [
    ["20","Safe completion","Exit on every public map"],
    ["20","Pathfinding","BFS/Dijkstra and path recovery"],
    ["15","Replanning","Use the latest Observation"],
    ["10","Energy check","Verify safe-return energy"],
    ["25","Performance","Score on released maps + code quality"],
    ["10","Design note","Complexity and failure analysis"]
  ],
  submissionRules: [
    "Edit and submit only student_policy.py from the released stage package. Do not modify agent.py.",
    "Do not modify the engine, maps, tests, runner, or configuration files.",
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
{number:"01",week:"WEEK 1",day:"TUESDAY",title:"TREE PLANNING FOUNDATIONS",unlocked:true,tagline:"Four public tree maps: path recovery, detours, and safe return.",focus:"BFS/DFS · Path recovery · Energy feasibility",repositoryUrl:"dist/week1_tuesday.zip?v=viewer-20260821",objectives:["Implement should_collect(obs, treasure, state): compare treasure reward with collection, detour, and safe-exit cost.","Implement select_target(obs, state): choose the most profitable next destination — a treasure or the exit.","Use the provided bfs_path from policy_helpers to route between any two cells on the tree.","Test on all four released tree maps without modifying agent.py."],deliverables:["student_policy.py","Short BFS/DFS complexity note","Score table for all four maps"],evaluation:{label:"TUESDAY EVALUATION",title:"Exit safely on four maps, then improve the score.",text:"The starter can reach the exit. Stronger policies collect profitable treasure without risking a zero-score run."}},
{number:"02",week:"WEEK 1",day:"THURSDAY",title:"GLOBAL TREE OPTIMIZATION",unlocked:false,tagline:"Five advanced maps: shared paths, subsets, and visit order.",focus:"Tree DP · Subset search · Branch-and-bound",repositoryUrl:"dist/week1_thursday.zip?v=viewer-20260821",objectives:["Implement plan_targets(obs, state): compute a global visit order for a profitable treasure subset ending at the exit.","Implement should_collect(obs, treasure, state): decide whether to collect when the agent arrives at a treasure.","Account for shared branch travel costs — nearest-first and isolated value/cost ratios are not optimal.","Test on all five released advanced tree maps."],deliverables:["student_policy.py","Greedy counterexample explanation","Score and runtime table for all five maps"],evaluation:{label:"THURSDAY EVALUATION",title:"Optimize the complete expedition on five public trees.",text:"The API is unchanged from Tuesday, but high scores require global rather than local decisions."}},
{number:"03",week:"WEEK 2",day:"TUESDAY",title:"WEIGHTED GRAPH ROUTES",unlocked:false,tagline:"Four public weighted maps: hop count replaced by terrain cost.",focus:"Dijkstra · Priority queue",repositoryUrl:"dist/week2_tuesday.zip?v=20260829",objectives:["Implement should_collect(obs, treasure, state): compare treasure reward against terrain-aware exit cost.","Implement select_target(obs, state): pick the next target using Dijkstra shortest-path costs.","Use the provided dijkstra_path from policy_helpers to compute weighted routes.","Test on all four released weighted maps — the fewest-step path is not always the cheapest."],deliverables:["student_policy.py","Dijkstra complexity note","Route-cost tests"],evaluation:{label:"PRACTICE EVALUATION",title:"Solve four released weighted maps.",text:"Mud and water are public; BFS by hop count can be expensive."}},
{number:"04",week:"WEEK 2",day:"THURSDAY",title:"PRIZE-COLLECTING GRAPH",unlocked:false,tagline:"Five cyclic weighted maps: treasure subset and visit-order planning.",focus:"Multi-target routing · Energy budget",repositoryUrl:"dist/week2_thursday.zip?v=20260829",objectives:["Implement plan_targets(obs, state): select a feasible treasure subset and optimize visit order using Dijkstra costs.","Implement should_collect(obs, treasure, state): decide at collection time whether to proceed or adjust the plan.","Account for cyclic graph routes — optimize the full expedition ending at the exit, not individual legs.","Test on all five released cyclic weighted graphs."],deliverables:["student_policy.py","Optimization design note","Ablation table"],evaluation:{label:"CHALLENGE EVALUATION",title:"Maximize score on five public general graphs.",text:"All inputs are known; global route optimization is the difficulty."}},
{number:"05",week:"WEEK 3",day:"TUESDAY",title:"HIDDEN FINAL CHALLENGE",unlocked:false,tagline:"One public practice map, private hidden seeds: implement two risk-aware policy rules.",focus:"Online decision rules · Hidden values · Energy safety",repositoryUrl:"dist/week3_tuesday.zip?v=20260829",objectives:["Implement should_collect(obs, treasure, exit_cost, state): weigh treasure value against exit cost, collection cost (1), and your SAFETY_MARGIN.","Implement should_continue_exploring(obs, frontier, cost_to_frontier, cost_frontier_to_exit, state): decide if one more frontier step is energy-safe.","Test on robustness_practice.json — your rules must generalize to private hidden-seed maps.","Unobserved cells (?) are not assumed passable; the exit is None until revealed."],deliverables:["student_policy.py","Design note explaining your two decision rules"],evaluation:{label:"FINAL EVALUATION",title:"Three-hour integrated lab: your policy runs on hidden private maps.",text:"Thursday is presentation only — no new code. Evaluation weighs score, exit rate, energy management, and robustness across hidden seeds."}}
];

window.SITE_CONTENT.stageRules = [
["The package contains four released maps: warmup, two branches, greedy trap, and energy budget.","The map, exit, treasure locations, and treasure values are fully public.","Every released map is a connected tree with one unique simple path between reachable cells.","Every move costs 1 energy, and COLLECT costs 1 additional energy.","Entering the exit ends the run immediately; collected treasure counts only after a successful exit.","The agent must reserve enough energy for the complete route to the exit.","Use --view to animate the map, --delay to control speed, and --no-clear to preserve every frame.","Submit student_policy.py unchanged across all four maps; do not modify agent.py."],
["All Week 1 Tuesday rules and the same Observation/Action API remain in effect.","The package contains five advanced maps: shared branch, value trap, subset order, large tree, and challenge.","Treasure branches may share travel cost and must not be evaluated as independent round trips.","Nearest-first, highest-value-first, and isolated value-to-cost ratio are not guaranteed to be optimal.","The agent must choose a feasible treasure subset and, when relevant, its visit order.","Exact search, tree DP, subset DP, branch-and-bound, and justified heuristics are allowed.","Use --view to animate the map, --delay to control speed, and --no-clear to preserve every frame.","All information remains public; the difficulty is global optimization rather than uncertainty.","Submit student_policy.py unchanged across all five maps; do not modify agent.py."],
["The package contains four public weighted maps: terrain choice, cycle detour, water crossing, and weighted maze.","Walkable cells form a weighted general graph and may contain cycles.","Terrain cost is charged when a cell is entered: normal/start/exit/treasure 1, mud 4, and water 7.","COLLECT costs 1 additional energy; the fewest-step path may not be the lowest-energy path.","The exit ends the run immediately and may not be used as an intermediate waypoint.","Submit student_policy.py unchanged across all four released maps; do not modify agent.py."],
["All Week 2 Tuesday action, terrain, scoring, and submission rules remain in effect.","The package contains five public cyclic weighted graphs.","The agent must select a feasible treasure subset and its visit order on a cyclic graph.","Optimize the complete route ending at the exit, not one treasure or one leg in isolation.","Exact search, subset DP, branch-and-bound, beam search, and justified heuristics are allowed.","Submit student_policy.py unchanged across all five maps; map-name and layout hardcoding are prohibited."],
["This is the three-hour integrated final. Thursday is presentation only — no new code after this lab.","The package contains one public practice map: robustness_practice.json. Private evaluation uses hidden seeds not distributed to students.","Edit and submit only student_policy.py. The fixed agent.py handles fog, frontier search, Dijkstra routing, and online replanning.","Implement should_collect(obs, treasure, exit_cost, state): compare treasure.value against exit cost, collection cost (1), and your SAFETY_MARGIN constant.","Implement should_continue_exploring(obs, frontier, cost_to_frontier, cost_frontier_to_exit, state): compare total travel cost against remaining energy.","Unobserved cells are ?; they are NOT assumed passable. The exit is None until revealed.","Hardcoded coordinates, map fingerprints, map names, and private seed detection are prohibited.","No state or information may be shared between separate evaluation runs."]
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
  badge: "6시간 실습",
  title: "탐험하라.",
  subtitle: "수집하라. 귀환하라.",
  description: "각 단계마다 범용 에이전트를 하나 제작하세요. 배포된 모든 맵에서 코드 수정 없이 실행하고, 수익성 있는 보물을 수집하면서 출구까지의 안전한 경로를 항상 확보하세요.",
  labHours: "6H", initialEnergy: "MAP", submission: "student_policy.py",
  pythonVersion: "Python 3.11+",
  command: "python -m treasure_explorer --map maps/warmup.json --agent agent.py --view",
  scoreFormula: "50 출구 보너스 + 보물 가치 + 남은 에너지 - 5 × 무효 행동",
  noExitRule: "출구 미도달 시 점수 없음",
  missionLabel: "01 / 임무",
  missionTitle: "하나의 에이전트. 단계의 모든 맵.",
  missionDescription: "현재 Observation을 읽고, 유효한 Action 하나를 선택하고, 반복하세요.",
  process: [["01","관측","맵 · 에너지"],["02","추정","가치 · 귀환 비용"],["03","계획","목표 · 경로"],["04","행동","행동 하나"]],
  rules: [
    {number:"규칙 01",title:"단계마다 정보가 달라집니다",text:"1주차 맵은 공개됩니다. 3주차는 각 Observation에 포함된 정보만 공개됩니다."},
    {number:"규칙 02",title:"귀환이 먼저입니다",text:"봇이 출구에 도달해야만 보물 점수가 인정됩니다."},
    {number:"규칙 03",title:"에너지를 관리하세요",text:"일반: 1 · 진흙: 4 · 물: 7 · 수집: 1"}
  ],
  schedule: [
    ["00:00","점검","엔진을 실행하고 Observation을 확인하세요."],
    ["00:40","경로","BFS로 경로를 구축하고 복원하세요."],
    ["02:10","가중치","지형 비용을 위해 Dijkstra로 업그레이드하세요."],
    ["03:10","상태","미탐지·탐지·수집된 보물을 추적하세요."],
    ["04:20","안전","귀환에 필요한 에너지를 확인하세요."],
    ["05:20","테스트","공개 맵을 실행하고 실패를 분석하세요."]
  ],
  rubric: [
    ["20","안전 완주","모든 공개 맵에서 출구 도달"],
    ["20","경로 탐색","BFS/Dijkstra 및 경로 복원"],
    ["15","재계획","최신 Observation 활용"],
    ["10","에너지 확인","안전한 귀환 에너지 검증"],
    ["25","성능","배정 맵 점수 및 코드 품질"],
    ["10","설계 노트","복잡도 및 실패 분석"]
  ],
  submissionRules: [
    "배포된 단계 패키지의 student_policy.py만 수정하여 제출하세요. agent.py는 수정하지 마세요.",
    "엔진, 맵, 테스트, 러너, 설정 파일은 수정하지 마세요.",
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
  {number:"01",week:"1주차",day:"화요일",title:"트리 계획 기초",unlocked:true,tagline:"공개 트리 맵 4개: 경로 복원, 우회, 안전 귀환.",focus:"BFS/DFS · 경로 복원 · 에너지 타당성",repositoryUrl:"dist/week1_tuesday.zip?v=viewer-20260821",objectives:["should_collect(obs, treasure, state) 구현: 보물 보상을 수집·우회·안전 출구 비용과 비교하세요.","select_target(obs, state) 구현: 가장 수익성 높은 다음 목표(보물 또는 출구)를 선택하세요.","policy_helpers의 bfs_path를 사용해 트리 위 임의의 두 셀 사이를 경로 탐색하세요.","agent.py를 수정하지 않고 배포된 트리 맵 4개 전체에서 테스트하세요."],deliverables:["student_policy.py","짧은 BFS/DFS 복잡도 노트","4개 맵 점수 표"],evaluation:{label:"화요일 평가",title:"4개 맵에서 안전하게 탈출한 뒤 점수를 높이세요.",text:"스타터 정책은 출구에 도달할 수 있습니다. 더 강한 정책은 0점 위험 없이 수익성 있는 보물을 수집합니다."}},
  {number:"02",week:"1주차",day:"목요일",title:"전역 트리 최적화",unlocked:false,tagline:"고급 맵 5개: 공유 경로, 부분집합, 방문 순서.",focus:"트리 DP · 부분집합 탐색 · Branch-and-Bound",repositoryUrl:"dist/week1_thursday.zip?v=viewer-20260821",objectives:["plan_targets(obs, state) 구현: 출구에서 끝나는 수익성 있는 보물 부분집합의 전역 방문 순서를 계산하세요.","should_collect(obs, treasure, state) 구현: 에이전트가 보물에 도달했을 때 수집 여부를 결정하세요.","공유 분기 이동 비용을 고려하세요 — 최근접·최고가·비율 탐욕은 최적이 아닙니다.","배포된 고급 트리 맵 5개 전체에서 테스트하세요."],deliverables:["student_policy.py","탐욕 반례 설명","5개 맵 점수 및 런타임 표"],evaluation:{label:"목요일 평가",title:"공개 트리 5개에서 전체 탐험을 최적화하세요.",text:"API는 화요일과 동일하지만, 높은 점수는 지역이 아닌 전역 결정이 필요합니다."}},
  {number:"03",week:"2주차",day:"화요일",title:"가중 그래프 경로",unlocked:false,tagline:"공개 가중 맵 4개: 단순 이동 횟수 대신 지형 비용.",focus:"Dijkstra · 우선순위 큐",repositoryUrl:"dist/week2_tuesday.zip?v=20260829",objectives:["should_collect(obs, treasure, state) 구현: 지형 인식 출구 비용 대비 보물 보상을 비교하세요.","select_target(obs, state) 구현: Dijkstra 최단 경로 비용으로 다음 목표를 선택하세요.","policy_helpers의 dijkstra_path를 사용해 가중 경로를 계산하세요.","배포된 가중 맵 4개 전체에서 테스트하세요 — 이동 횟수 최소 경로가 항상 가장 저렴하지는 않습니다."],deliverables:["student_policy.py","Dijkstra 복잡도 노트","경로 비용 테스트"],evaluation:{label:"실습 평가",title:"배포된 가중 맵 4개를 해결하세요.",text:"진흙과 물이 공개됩니다. 이동 횟수 기반 BFS는 비용이 클 수 있습니다."}},
  {number:"04",week:"2주차",day:"목요일",title:"상금 수집 그래프",unlocked:false,tagline:"사이클 가중 맵 5개: 보물 부분집합과 방문 순서 계획.",focus:"다중 목표 경로 탐색 · 에너지 예산",repositoryUrl:"dist/week2_thursday.zip?v=20260829",objectives:["plan_targets(obs, state) 구현: Dijkstra 비용을 사용해 실행 가능한 보물 부분집합을 선택하고 방문 순서를 최적화하세요.","should_collect(obs, treasure, state) 구현: 수집 시점에 진행 또는 계획 조정 여부를 결정하세요.","사이클 그래프 경로를 고려하세요 — 개별 구간이 아닌 출구에서 끝나는 전체 탐험을 최적화하세요.","배포된 사이클 가중 그래프 5개 전체에서 테스트하세요."],deliverables:["student_policy.py","최적화 설계 노트","Ablation 표"],evaluation:{label:"도전 평가",title:"공개 일반 그래프 5개에서 점수를 최대화하세요.",text:"모든 입력이 공개됩니다. 전역 경로 최적화가 핵심입니다."}},
  {number:"05",week:"3주차",day:"화요일",title:"통합 숨겨진 최종 도전",unlocked:false,tagline:"공개 연습 맵 1개, 비공개 시드 평가: 두 가지 위험 인식 정책 규칙을 구현하세요.",focus:"온라인 결정 규칙 · 숨겨진 가치 · 에너지 안전",repositoryUrl:"dist/week3_tuesday.zip?v=20260829",objectives:["should_collect(obs, treasure, exit_cost, state) 구현: 보물 가치를 출구 비용, 수집 비용(1), SAFETY_MARGIN과 비교하세요.","should_continue_exploring(obs, frontier, cost_to_frontier, cost_frontier_to_exit, state) 구현: 복귀 비용을 감안해 프론티어 한 번 더 탐색이 에너지상 안전한지 판단하세요.","robustness_practice.json으로 테스트하세요 — 규칙은 비공개 숨겨진 시드 맵으로 일반화돼야 합니다.","관측되지 않은 셀(?)은 통과 가능하다고 가정하지 마세요. 출구는 공개될 때까지 None입니다."],deliverables:["student_policy.py","두 가지 결정 규칙을 설명하는 설계 노트"],evaluation:{label:"최종 평가",title:"3시간 통합 실험: 비공개 숨겨진 맵에서 정책이 실행됩니다.",text:"목요일은 발표만 진행됩니다 — 새로운 코드는 없습니다. 평가는 점수·출구 도달률·에너지 관리·숨겨진 시드 강건성을 종합합니다."}}
];

window.SITE_CONTENT_KO.stageRules = [
  ["패키지에는 4개의 배포 맵이 포함됩니다: warmup, 두 분기, 탐욕 함정, 에너지 예산.","맵, 출구, 보물 위치와 보물 가치가 모두 공개됩니다.","배포된 모든 맵은 연결 트리로, 도달 가능한 두 셀 사이에는 유일한 단순 경로가 하나만 있습니다.","모든 이동은 에너지 1을 소비하며, COLLECT는 에너지 1을 추가로 소비합니다.","출구에 진입하면 즉시 게임이 종료됩니다. 수집한 보물은 성공적으로 출구에 도달한 후에만 점수로 인정됩니다.","에이전트는 출구까지의 완전한 경로에 필요한 에너지를 반드시 예비해야 합니다.","--view로 맵을 애니메이션으로 확인하고, --delay로 속도를 조절하고, --no-clear로 모든 프레임을 유지할 수 있습니다.","student_policy.py를 4개 맵 전체에서 수정 없이 제출하세요. agent.py는 수정하지 마세요."],
  ["1주차 화요일의 모든 규칙과 동일한 Observation/Action API가 유지됩니다.","패키지에는 5개의 고급 맵이 포함됩니다: 공유 분기, 가치 함정, 부분집합 순서, 큰 트리, 챌린지.","보물 분기는 이동 비용을 공유할 수 있으므로 독립적인 왕복으로 평가해서는 안 됩니다.","최근접·최고가·독립 가치-비용 비율은 최적이 보장되지 않습니다.","에이전트는 실행 가능한 보물 부분집합과 관련된 경우 방문 순서를 선택해야 합니다.","완전 탐색, 트리 DP, 부분집합 DP, branch-and-bound, 정당화된 휴리스틱이 허용됩니다.","--view로 맵을 애니메이션으로 확인하고, --delay로 속도를 조절하고, --no-clear로 모든 프레임을 유지할 수 있습니다.","모든 정보가 공개됩니다. 난이도는 전역 최적화에 있습니다.","student_policy.py를 5개 맵 전체에서 수정 없이 제출하세요. agent.py는 수정하지 마세요."],
  ["패키지에는 4개의 공개 가중 맵이 포함됩니다: 지형 선택, 사이클 우회, 물 횡단, 가중 미로.","이동 가능한 셀은 가중 일반 그래프를 형성하며 사이클을 포함할 수 있습니다.","셀에 진입할 때 지형 비용이 부과됩니다: 일반/시작/출구/보물 1, 진흙 4, 물 7.","COLLECT는 에너지 1을 추가 소비합니다. 이동 횟수가 가장 적은 경로가 에너지 최소 경로가 아닐 수 있습니다.","출구는 게임을 즉시 종료하며 중간 경유지로 사용할 수 없습니다.","배포된 4개 맵 전체에서 수정 없이 실행되는 student_policy.py를 제출하세요. agent.py는 수정하지 마세요."],
  ["2주차 화요일의 모든 행동, 지형, 채점, 제출 규칙이 유지됩니다.","패키지에는 5개의 공개 사이클 가중 그래프가 포함됩니다.","에이전트는 사이클 그래프에서 실행 가능한 보물 부분집합과 방문 순서를 선택해야 합니다.","보물 하나나 구간 하나가 아닌, 출구에서 끝나는 전체 경로를 최적화하세요.","완전 탐색, 부분집합 DP, branch-and-bound, beam search, 정당화된 휴리스틱이 허용됩니다.","동일한 student_policy.py가 5개 맵 모두에서 수정 없이 실행돼야 합니다. 맵 이름과 레이아웃 하드코딩은 금지됩니다."],
  ["이것은 3시간 통합 최종 실험입니다. 목요일은 발표만 진행됩니다 — 이 실험 이후 새로운 코드는 없습니다.","패키지에는 공개 연습 맵 1개(robustness_practice.json)가 포함됩니다. 비공개 평가는 학생에게 배포되지 않은 비공개 시드를 사용합니다.","student_policy.py만 수정하여 제출하세요. 고정된 agent.py는 안개, 프론티어 탐색, Dijkstra 경로 탐색, 온라인 재계획을 처리합니다.","should_collect(obs, treasure, exit_cost, state) 구현: treasure.value를 출구 비용, 수집 비용(1), SAFETY_MARGIN 상수와 비교하세요.","should_continue_exploring(obs, frontier, cost_to_frontier, cost_frontier_to_exit, state) 구현: 총 이동 비용을 남은 에너지와 비교하세요.","관측되지 않은 셀은 ?입니다. 통과 가능하다고 가정하지 마세요. 출구는 공개될 때까지 None입니다.","하드코딩된 좌표, 맵 지문, 맵 이름, 비공개 시드 탐지는 금지됩니다.","독립적인 평가 실행 사이에 상태나 정보를 공유할 수 없습니다."]
];

window.SITE_CONTENT_KO.stageCommands = window.SITE_CONTENT.stageCommands;
window.SITE_CONTENT_KO.batchCommands = window.SITE_CONTENT.batchCommands;
