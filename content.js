// Edit this file and click "Commit changes". GitHub Pages updates automatically.
window.SITE_CONTENT = {
  semester: "Problem Solving Techniques · Fall 2026",
  badge: "6-HOUR LAB",
  title: "Explore.",
  subtitle: "Collect. Return.",
  description: "Build one generic agent per stage. Run it unchanged across every released map, collect profitable treasure, and always preserve a safe route to the exit.",
  labHours: "6H", initialEnergy: "MAP", submission: "agent.py",
  pythonVersion: "Python 3.11+",
  command: "python -m treasure_explorer --map maps/warmup.json --agent agent.py --view",
  scoreFormula: "50 EXIT BONUS + TREASURE + ENERGY LEFT - 5 INVALID",
  noExitRule: "NO EXIT, NO SCORE",
  missionLabel: "01 / MISSION",
  missionTitle: "One agent. Every map in the stage.",
  missionDescription: "Read the current Observation, select one valid Action, and repeat.",
  process: [["01","OBSERVE","Map · Energy"],["02","ESTIMATE","Value · Return cost"],["03","PLAN","Target · Route"],["04","ACT","One action"]],
  rules: [
    {number:"RULE 01",title:"Information changes by stage",text:"Week 1?? maps are public. Week 3 reveals only the information included in each Observation."},
    {number:"RULE 02",title:"Return first",text:"Treasure counts only after the bot reaches the exit."},
    {number:"RULE 03",title:"Budget energy",text:"Normal: 1 · Mud: 4 · Water: 7 · Collect: 1"}
  ],
  schedule: [
    ["00:00","Inspect","Run the engine and inspect Observation."],
    ["00:40","Route","Build and recover a path with BFS."],
    ["02:10","Weight","Upgrade to Dijkstra for terrain costs."],
    ["03:10","State","Track unknown, known, and collected treasure."],
    ["04:20","Safety","Check the energy needed to return."],
    ["05:20","Test","Run public maps and review failures."]
  ],
  rubric: [
    ["20","Safe finish","Reach the exit on every public map"],
    ["20","Pathfinding","BFS/Dijkstra and path recovery"],
    ["15","Replanning","Use the latest observation"],
    ["10","Energy check","Verify a safe return"],
    ["25","Performance","Assigned-map score and code quality"],
    ["10","Design note","Complexity and failure analysis"]
  ],
  weeks: [
    {
      number: "01", title: "KEYED TREE ESCAPE",
      tagline: "Build a search tree, collect the right items, and reach the exit.",
      focus: "DFS/BFS parent tree · Provided maps",
      repositoryUrl: "https://github.com/rata-max/treasure-explorer-challenge/tree/main/treasure-explorer-week1-tree-escape",
      objectives: ["Build a DFS or BFS parent tree over the maze.", "Recover the unique path to a key, useful batteries, and the exit.", "Manage energy and reach the exit on all three released maps."],
      deliverables: ["student/agent.py", "Complexity and path-recovery note", "Results on easy, medium, and hard maps"],
      evaluation: {
        label: "PRACTICE EVALUATION",
        title: "Solve the three provided tree-maze tasks.",
        text: "The easy map needs a key path. The medium and hard maps require battery-aware planning. Week 1 uses no unseen hidden maps."
      }
    },
    {
      number: "02", title: "RISK-AWARE ONLINE PLANNER",
      tagline: "Balance expected reward against uncertain travel costs.",
      focus: "Intermediate practice · Provided scenarios",
      repositoryUrl: "",
      objectives: ["Model expected and worst-case terrain costs.", "Adjust risk using remaining energy.", "Choose and abandon multi-treasure plans online."],
      deliverables: ["student/agent.py", "Risk model description", "Week 1 comparison"],
      evaluation: {
        label: "PRACTICE EVALUATION",
        title: "Solve the provided risk-aware planning tasks.",
        text: "Week 2 is evaluated with the released scenarios and stated requirements. Use the feedback to prepare the final agent."
      }
    },
    {
      number: "03", title: "ROBUST EXPLORER CHAMPIONSHIP",
      tagline: "Generalize across unseen maps, costs, and treasure values.",
      focus: "Hidden-map robustness",
      repositoryUrl: "",
      objectives: ["Generalize without map-specific hardcoding.", "Improve average score, exit rate, and worst-case behavior.", "Keep every decision within the runtime limit."],
      deliverables: ["Final student/agent.py", "Two-page final report", "Failure and ablation analysis"],
      evaluation: {
        label: "FINAL EVALUATION",
        title: "The final agent runs on unseen hidden maps.",
        text: "Only Week 3 uses unseen hidden maps and seeds. Evaluation considers score, exit rate, robustness, invalid actions, and runtime."
      }
    }
  ],
  submissionRules: [
    "Modify and submit the root-level agent.py from the released stage package.",
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

/* Six sequential releases. TA: unlock only the next item. Keep unreleased ZIPs off the public branch. */
window.SITE_CONTENT.stages = [
{number:"01",week:"WEEK 1",day:"TUESDAY",title:"TREE PLANNING FOUNDATIONS",unlocked:true,tagline:"Four public tree maps: path recovery, detours, and safe return.",focus:"BFS/DFS - Path recovery - Energy feasibility",repositoryUrl:"dist/week1_tuesday.zip?v=viewer-20260821",objectives:["Solve all four released public tree maps.","Recover the unique path between relevant cells.","Compare treasure reward with collection, detour, and safe-exit cost.","Recognize why nearest-first can fail on the greedy-trap map."],deliverables:["One generic agent.py","Short BFS/DFS complexity note","Score table for all four maps"],evaluation:{label:"TUESDAY EVALUATION",title:"Exit safely on four maps, then improve the score.",text:"The starter can reach the exit. Stronger agents collect profitable treasure without risking a zero-score run."}},
{number:"02",week:"WEEK 1",day:"THURSDAY",title:"GLOBAL TREE OPTIMIZATION",unlocked:false,tagline:"Five advanced maps: shared paths, subsets, and visit order.",focus:"Tree DP - Subset search - Branch-and-bound",repositoryUrl:"dist/week1_thursday.zip?v=viewer-20260821",objectives:["Solve all five released advanced tree maps.","Identify nearest-first, highest-value-first, and ratio-greedy failures.","Account for travel costs shared by treasures in the same branch.","Select a feasible treasure subset and its visit order."],deliverables:["One improved generic agent.py","Greedy counterexample explanation","Score and runtime table for all five maps"],evaluation:{label:"THURSDAY EVALUATION",title:"Optimize the complete expedition on five public trees.",text:"The API is unchanged from Tuesday, but high scores require global rather than local decisions."}},
{number:"03",week:"WEEK 2",day:"TUESDAY",title:"WEIGHTED GRAPH ROUTES",unlocked:false,tagline:"Four public weighted maps replace simple hop count with terrain cost.",focus:"Dijkstra - Priority queue",repositoryUrl:"dist/week2_tuesday.zip?v=20260829",objectives:["Solve all four released weighted maps.","Compute terrain-aware shortest paths.","Reconstruct weighted routes.","Compare treasure detours by true cost."],deliverables:["One generic agent.py","Dijkstra complexity note","Route-cost tests"],evaluation:{label:"PRACTICE EVALUATION",title:"Solve four released weighted maps.",text:"Mud and water are public; BFS by hop count can be expensive."}},
{number:"04",week:"WEEK 2",day:"THURSDAY",title:"PRIZE-COLLECTING GRAPH",unlocked:false,tagline:"Five cyclic weighted maps require treasure subset and visit-order planning.",focus:"Multi-target routing - Energy budget",repositoryUrl:"dist/week2_thursday.zip?v=20260829",objectives:["Solve all five released weighted graphs.","Select a feasible treasure subset.","Optimize visit order.","Trade search quality against runtime."],deliverables:["One generic agent.py","Optimization design note","Ablation table"],evaluation:{label:"CHALLENGE EVALUATION",title:"Maximize score on five public general graphs.",text:"All inputs are known; global route optimization is the difficulty."}},
{number:"05",week:"WEEK 3",day:"TUESDAY",title:"FOG AND REPLANNING",unlocked:false,tagline:"Four fog maps reveal terrain incrementally and require online replanning.",focus:"Frontiers - Online replanning",repositoryUrl:"dist/week3_tuesday.zip?v=20260829",objectives:["Solve all four released fog maps.","Maintain a partial world model.","Explore useful frontier cells.","Replan after terrain revelation."],deliverables:["One generic agent.py","Replanning trace","Failure analysis"],evaluation:{label:"PRACTICE EVALUATION",title:"Adapt on four released fog maps.",text:"The agent receives only its current cumulative observation on every turn."}},
{number:"06",week:"WEEK 3",day:"THURSDAY",title:"HIDDEN FINAL CHALLENGE",unlocked:false,tagline:"Three practice maps prepare one agent for unseen hidden-seed evaluation.",focus:"Exploration vs exploitation - Robustness",repositoryUrl:"dist/week3_thursday.zip?v=20260829",objectives:["Generalize from three practice maps to unseen evaluation maps.","Balance information gain and safe return.","Handle hidden treasure values without map-name hardcoding.","Improve average score and exit rate."],deliverables:["Final generic agent.py","Two-page report","Ablation and failure analysis"],evaluation:{label:"FINAL EVALUATION",title:"Run one agent on unseen seeded maps.",text:"Evaluation combines score, exit rate, robustness, invalid actions, and runtime."}}
];

window.SITE_CONTENT.stageRules = [
["The package contains four released maps: warmup, two branches, greedy trap, and energy budget.","The map, exit, treasure locations, and treasure values are fully public.","Every released map is a connected tree with one unique simple path between reachable cells.","Every move costs 1 energy, and COLLECT costs 1 additional energy.","Entering the exit ends the run immediately; collected treasure counts only after a successful exit.","The agent must reserve enough energy for the complete route to the exit.","Use --view to animate the map, --delay to control speed, and --no-clear to preserve every frame.","Submit one generic agent.py that runs unchanged on all four maps."],
["All Week 1 Tuesday rules and the same Observation/Action API remain in effect.","The package contains five advanced maps: shared branch, value trap, subset order, large tree, and challenge.","Treasure branches may share travel cost and must not be evaluated as independent round trips.","Nearest-first, highest-value-first, and isolated value-to-cost ratio are not guaranteed to be optimal.","The agent must choose a feasible treasure subset and, when relevant, its visit order.","Exact search, tree DP, subset DP, branch-and-bound, and justified heuristics are allowed.","Use --view to animate the map, --delay to control speed, and --no-clear to preserve every frame.","All information remains public; the difficulty is global optimization rather than uncertainty.","The route must reach the exit or the run scores zero, and one generic agent.py must handle all five maps."],
["The package contains four public weighted maps: terrain choice, cycle detour, water crossing, and weighted maze.","Walkable cells form a weighted general graph and may contain cycles.","Terrain cost is charged when a cell is entered: normal/start/exit/treasure 1, mud 4, and water 7.","COLLECT costs 1 additional energy; the fewest-step path may not be the lowest-energy path.","The exit ends the run immediately and may not be used as an intermediate waypoint.","Submit one generic agent.py that runs unchanged on all four released maps."],
["All Week 2 Tuesday action, terrain, scoring, and submission rules remain in effect.","The package contains five public cyclic weighted graphs.","The agent must select a feasible treasure subset and its visit order on a cyclic graph.","Optimize the complete route ending at the exit, not one treasure or one leg in isolation.","Exact search, subset DP, branch-and-bound, beam search, and justified heuristics are allowed.","The same agent.py must run unchanged on all five maps; map-name and layout hardcoding are prohibited."],
["The package contains four partially observable fog maps.","Each decision may use the current Observation and memory accumulated within the same run.","Unobserved cells are shown as ?; unknown does not mean normal, safe, blocked, or passable.","The exit remains None until revealed; revealed information is cumulative within a run.","Separate map runs begin with fresh agent state.","Select exploration frontiers and replan whenever new information changes route cost or feasibility.","Submit one generic agent.py that runs unchanged on all four released fog maps."],
["All Week 3 Tuesday observation, memory, action, scoring, and submission rules remain in effect.","The package contains three hidden-value practice maps; treasure values are None until the treasure is reached.","The submitted agent runs unchanged on the practice maps and unseen maps generated from private seeds.","Hardcoded coordinates, map fingerprints, seed detection, file access, networking, subprocesses, reflection, and side channels are prohibited.","No state or information may be shared between independent evaluation runs.","Evaluation emphasizes normalized score, exit rate, invalid actions, runtime, and worst-case robustness.","Exact private seed set and evaluation maps are not distributed to students."]
];

/* Commands shown on the homepage and assignment pages. */
window.SITE_CONTENT.stageCommands = [
  "python -m treasure_explorer --map maps/warmup.json --agent agent.py --view",
  "python -m treasure_explorer --map maps/shared_branch.json --agent agent.py --view",
  "python -m treasure_explorer --map maps/terrain_choice.json --agent agent.py --view",
  "python -m treasure_explorer --map maps/pair_or_prize.json --agent agent.py --view",
  "python -m treasure_explorer --map maps/fog_corridor.json --agent agent.py --view",
  "python -m treasure_explorer --map maps/hidden_values_a.json --agent agent.py --view"
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
  labHours: "6H", initialEnergy: "MAP", submission: "agent.py",
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
  weeks: [
    {
      number:"01", title:"KEYED TREE ESCAPE",
      tagline:"탐색 트리를 구축하고, 필요한 아이템을 수집한 뒤, 출구에 도달하세요.",
      focus:"DFS/BFS 부모 트리 · 공개 맵",
      repositoryUrl:"https://github.com/rata-max/treasure-explorer-challenge/tree/main/treasure-explorer-week1-tree-escape",
      objectives:["미로 전체를 DFS 또는 BFS 부모 트리로 탐색하세요.","열쇠, 유용한 배터리, 출구까지의 유일한 경로를 복원하세요.","에너지를 관리하며 배포된 세 맵 모두에서 출구에 도달하세요."],
      deliverables:["student/agent.py","복잡도 및 경로 복원 노트","쉬움·보통·어려움 맵 결과"],
      evaluation:{label:"실습 평가",title:"배포된 세 가지 트리 미로 과제를 해결하세요.",text:"쉬운 맵은 열쇠 경로가 필요하고, 보통·어려운 맵은 배터리 인식 계획이 필요합니다. 1주차에는 숨겨진 맵을 사용하지 않습니다."}
    },
    {
      number:"02", title:"RISK-AWARE ONLINE PLANNER",
      tagline:"불확실한 이동 비용 대비 기대 보상의 균형을 맞추세요.",
      focus:"중간 실습 · 공개 시나리오",
      repositoryUrl:"",
      objectives:["기대 지형 비용과 최악의 경우 비용을 모델링하세요.","남은 에너지에 따라 위험도를 조정하세요.","다중 보물 계획을 온라인으로 선택하고 포기하세요."],
      deliverables:["student/agent.py","위험 모델 설명","1주차 비교"],
      evaluation:{label:"실습 평가",title:"배포된 위험 인식 계획 과제를 해결하세요.",text:"2주차는 배포된 시나리오와 명시된 요구사항으로 평가됩니다. 피드백을 활용해 최종 에이전트를 준비하세요."}
    },
    {
      number:"03", title:"ROBUST EXPLORER CHAMPIONSHIP",
      tagline:"미공개 맵, 비용, 보물 가치에 범용적으로 대응하세요.",
      focus:"숨겨진 맵 강건성",
      repositoryUrl:"",
      objectives:["맵별 하드코딩 없이 범용화하세요.","평균 점수, 출구 도달률, 최악의 경우를 개선하세요.","모든 결정을 런타임 제한 내에 유지하세요."],
      deliverables:["최종 student/agent.py","2쪽짜리 최종 보고서","실패 및 ablation 분석"],
      evaluation:{label:"최종 평가",title:"최종 에이전트가 미공개 숨겨진 맵에서 실행됩니다.",text:"3주차만 미공개 숨겨진 맵과 시드를 사용합니다. 점수·출구 도달률·강건성·무효 행동·런타임을 종합 평가합니다."}
    }
  ],
  submissionRules: [
    "배포된 단계 패키지의 루트 레벨 agent.py를 수정하여 제출하세요.",
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
  {number:"01",week:"1주차",day:"화요일",title:"트리 계획 기초",unlocked:true,tagline:"공개 트리 맵 4개: 경로 복원, 우회, 안전 귀환.",focus:"BFS/DFS - 경로 복원 - 에너지 타당성",repositoryUrl:"dist/week1_tuesday.zip?v=viewer-20260821",objectives:["배포된 공개 트리 맵 4개를 모두 해결하세요.","관련 셀 사이의 유일한 경로를 복원하세요.","보물 보상을 수집·우회·안전 출구 비용과 비교하세요.","탐욕적 최근접 탐색이 greedy-trap 맵에서 실패하는 이유를 파악하세요."],deliverables:["범용 agent.py 하나","짧은 BFS/DFS 복잡도 노트","4개 맵 점수 표"],evaluation:{label:"화요일 평가",title:"4개 맵에서 안전하게 탈출한 뒤 점수를 높이세요.",text:"스타터 에이전트는 출구에 도달할 수 있습니다. 더 강한 에이전트는 0점 위험 없이 수익성 있는 보물을 수집합니다."}},
  {number:"02",week:"1주차",day:"목요일",title:"전역 트리 최적화",unlocked:false,tagline:"고급 맵 5개: 공유 경로, 부분집합, 방문 순서.",focus:"트리 DP - 부분집합 탐색 - Branch-and-Bound",repositoryUrl:"dist/week1_thursday.zip?v=viewer-20260821",objectives:["배포된 고급 트리 맵 5개를 모두 해결하세요.","최근접·최고가·비율 탐욕 실패를 파악하세요.","같은 분기에 있는 보물들이 공유하는 이동 비용을 고려하세요.","실행 가능한 보물 부분집합과 방문 순서를 선택하세요."],deliverables:["개선된 범용 agent.py 하나","탐욕 반례 설명","5개 맵 점수 및 런타임 표"],evaluation:{label:"목요일 평가",title:"공개 트리 5개에서 전체 탐험을 최적화하세요.",text:"API는 화요일과 동일하지만, 높은 점수는 지역이 아닌 전역 결정이 필요합니다."}},
  {number:"03",week:"2주차",day:"화요일",title:"가중 그래프 경로",unlocked:false,tagline:"공개 가중 맵 4개: 단순 이동 횟수 대신 지형 비용.",focus:"Dijkstra - 우선순위 큐",repositoryUrl:"dist/week2_tuesday.zip?v=20260829",objectives:["배포된 가중 맵 4개를 모두 해결하세요.","지형 인식 최단 경로를 계산하세요.","가중 경로를 복원하세요.","실제 비용으로 보물 우회를 비교하세요."],deliverables:["범용 agent.py 하나","Dijkstra 복잡도 노트","경로 비용 테스트"],evaluation:{label:"실습 평가",title:"배포된 가중 맵 4개를 해결하세요.",text:"진흙과 물이 공개됩니다. 이동 횟수 기반 BFS는 비용이 클 수 있습니다."}},
  {number:"04",week:"2주차",day:"목요일",title:"상금 수집 그래프",unlocked:false,tagline:"사이클 가중 맵 5개: 보물 부분집합과 방문 순서 계획.",focus:"다중 목표 경로 탐색 - 에너지 예산",repositoryUrl:"dist/week2_thursday.zip?v=20260829",objectives:["배포된 가중 그래프 5개를 모두 해결하세요.","실행 가능한 보물 부분집합을 선택하세요.","방문 순서를 최적화하세요.","탐색 품질과 런타임을 균형 있게 조절하세요."],deliverables:["범용 agent.py 하나","최적화 설계 노트","Ablation 표"],evaluation:{label:"도전 평가",title:"공개 일반 그래프 5개에서 점수를 최대화하세요.",text:"모든 입력이 공개됩니다. 전역 경로 최적화가 핵심입니다."}},
  {number:"05",week:"3주차",day:"화요일",title:"안개와 재계획",unlocked:false,tagline:"안개 맵 4개: 지형이 점진적으로 공개되고 온라인 재계획이 필요합니다.",focus:"프론티어 - 온라인 재계획",repositoryUrl:"dist/week3_tuesday.zip?v=20260829",objectives:["배포된 안개 맵 4개를 모두 해결하세요.","부분 세계 모델을 유지하세요.","유용한 프론티어 셀을 탐색하세요.","지형 공개 후 재계획하세요."],deliverables:["범용 agent.py 하나","재계획 추적","실패 분석"],evaluation:{label:"실습 평가",title:"배포된 안개 맵 4개에 적응하세요.",text:"에이전트는 매 턴 현재까지의 누적 Observation만 받습니다."}},
  {number:"06",week:"3주차",day:"목요일",title:"최종 숨겨진 도전",unlocked:false,tagline:"연습 맵 3개로 미공개 숨겨진 시드 평가를 준비하세요.",focus:"탐색 vs. 활용 - 강건성",repositoryUrl:"dist/week3_thursday.zip?v=20260829",objectives:["연습 맵 3개에서 미공개 평가 맵으로 범용화하세요.","정보 획득과 안전한 귀환을 균형 있게 조절하세요.","맵 이름 하드코딩 없이 숨겨진 보물 가치를 처리하세요.","평균 점수와 출구 도달률을 개선하세요."],deliverables:["최종 범용 agent.py","2쪽짜리 보고서","Ablation 및 실패 분석"],evaluation:{label:"최종 평가",title:"미공개 시드 맵에서 하나의 에이전트를 실행하세요.",text:"점수·출구 도달률·강건성·무효 행동·런타임을 종합 평가합니다."}}
];

window.SITE_CONTENT_KO.stageRules = [
  ["패키지에는 4개의 배포 맵이 포함됩니다: warmup, 두 분기, 탐욕 함정, 에너지 예산.","맵, 출구, 보물 위치와 보물 가치가 모두 공개됩니다.","배포된 모든 맵은 연결 트리로, 도달 가능한 두 셀 사이에는 유일한 단순 경로가 하나만 있습니다.","모든 이동은 에너지 1을 소비하며, COLLECT는 에너지 1을 추가로 소비합니다.","출구에 진입하면 즉시 게임이 종료됩니다. 수집한 보물은 성공적으로 출구에 도달한 후에만 점수로 인정됩니다.","에이전트는 출구까지의 완전한 경로에 필요한 에너지를 반드시 예비해야 합니다.","--view로 맵을 애니메이션으로 확인하고, --delay로 속도를 조절하고, --no-clear로 모든 프레임을 유지할 수 있습니다.","4개 맵 모두에서 변경 없이 실행되는 범용 agent.py 하나를 제출하세요."],
  ["1주차 화요일의 모든 규칙과 동일한 Observation/Action API가 유지됩니다.","패키지에는 5개의 고급 맵이 포함됩니다: 공유 분기, 가치 함정, 부분집합 순서, 큰 트리, 챌린지.","보물 분기는 이동 비용을 공유할 수 있으므로 독립적인 왕복으로 평가해서는 안 됩니다.","최근접·최고가·독립 가치-비용 비율은 최적이 보장되지 않습니다.","에이전트는 실행 가능한 보물 부분집합과 관련된 경우 방문 순서를 선택해야 합니다.","완전 탐색, 트리 DP, 부분집합 DP, branch-and-bound, 정당화된 휴리스틱이 허용됩니다.","--view로 맵을 애니메이션으로 확인하고, --delay로 속도를 조절하고, --no-clear로 모든 프레임을 유지할 수 있습니다.","모든 정보가 공개됩니다. 난이도는 전역 최적화에 있습니다.","경로는 출구에 도달해야 하며, 도달 못하면 점수가 0점입니다. 하나의 범용 agent.py가 5개 맵 모두를 처리해야 합니다."],
  ["패키지에는 4개의 공개 가중 맵이 포함됩니다: 지형 선택, 사이클 우회, 물 횡단, 가중 미로.","이동 가능한 셀은 가중 일반 그래프를 형성하며 사이클을 포함할 수 있습니다.","셀에 진입할 때 지형 비용이 부과됩니다: 일반/시작/출구/보물 1, 진흙 4, 물 7.","COLLECT는 에너지 1을 추가 소비합니다. 이동 횟수가 가장 적은 경로가 에너지 최소 경로가 아닐 수 있습니다.","출구는 게임을 즉시 종료하며 중간 경유지로 사용할 수 없습니다.","배포된 4개 맵 모두에서 변경 없이 실행되는 범용 agent.py 하나를 제출하세요."],
  ["2주차 화요일의 모든 행동, 지형, 채점, 제출 규칙이 유지됩니다.","패키지에는 5개의 공개 사이클 가중 그래프가 포함됩니다.","에이전트는 사이클 그래프에서 실행 가능한 보물 부분집합과 방문 순서를 선택해야 합니다.","보물 하나나 구간 하나가 아닌, 출구에서 끝나는 전체 경로를 최적화하세요.","완전 탐색, 부분집합 DP, branch-and-bound, beam search, 정당화된 휴리스틱이 허용됩니다.","동일한 agent.py가 5개 맵 모두에서 변경 없이 실행되어야 합니다. 맵 이름과 레이아웃 하드코딩은 금지됩니다."],
  ["패키지에는 4개의 부분 관측 안개 맵이 포함됩니다.","각 결정은 현재 Observation과 같은 실행 내에서 누적된 기억을 사용할 수 있습니다.","관측되지 않은 셀은 ?로 표시됩니다. 미지(unknown)는 일반, 안전, 차단, 통과 가능을 의미하지 않습니다.","출구는 공개될 때까지 None입니다. 공개된 정보는 실행 내에서 누적됩니다.","별도의 맵 실행은 에이전트 상태를 새로 시작합니다.","새로운 정보가 경로 비용이나 타당성을 변경할 때마다 탐색 프론티어를 선택하고 재계획하세요.","배포된 안개 맵 4개 모두에서 변경 없이 실행되는 범용 agent.py 하나를 제출하세요."],
  ["3주차 화요일의 모든 관측, 기억, 행동, 채점, 제출 규칙이 유지됩니다.","패키지에는 3개의 숨겨진 가치 연습 맵이 포함됩니다. 보물에 도달하기 전까지 보물 가치는 None입니다.","제출된 에이전트는 연습 맵과 비공개 시드로 생성된 미공개 맵 모두에서 변경 없이 실행됩니다.","하드코딩된 좌표, 맵 지문, 시드 감지, 파일 접근, 네트워크, 서브프로세스, 리플렉션, 사이드 채널은 금지됩니다.","독립적인 평가 실행 사이에 상태나 정보를 공유할 수 없습니다.","평가는 정규화된 점수, 출구 도달률, 무효 행동, 런타임, 최악의 경우 강건성을 중점으로 합니다.","정확한 비공개 시드 세트와 평가 맵은 학생에게 배포되지 않습니다."]
];

window.SITE_CONTENT_KO.stageCommands = window.SITE_CONTENT.stageCommands;
window.SITE_CONTENT_KO.batchCommands = window.SITE_CONTENT.batchCommands;
