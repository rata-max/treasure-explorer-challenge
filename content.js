// Edit this file and click "Commit changes". GitHub Pages updates automatically.
window.SITE_CONTENT = {
  semester: "Problem Solving Techniques 쨌 Fall 2026",
  badge: "6-HOUR LAB",
  title: "Explore.",
  subtitle: "Collect. Return.",
  description: "Build one generic agent per stage. Run it unchanged across every released map, collect profitable treasure, and always preserve a safe route to the exit.",
  labHours: "6H", initialEnergy: "MAP", submission: "agent.py",
  pythonVersion: "Python 3.11+",
  command: "python -m treasure_explorer --map maps/warmup.json --agent agent.py --view",
  scoreFormula: "50 EXIT BONUS + TREASURE + ENERGY LEFT - 5 횞 INVALID",
  noExitRule: "NO EXIT, NO SCORE",
  missionLabel: "01 / MISSION",
  missionTitle: "One agent. Every map in the stage.",
  missionDescription: "Read the current Observation, select one valid Action, and repeat. Week 1?? use public information; Week 3 introduces partial observability.",
  process: [["01","OBSERVE","Map 쨌 Energy"],["02","ESTIMATE","Value 쨌 Return cost"],["03","PLAN","Target 쨌 Route"],["04","ACT","One action"]],
  rules: [
    {number:"RULE 01",title:"Information changes by stage",text:"Week 1?? maps are public. Week 3 reveals only the information included in each Observation."},
    {number:"RULE 02",title:"Return first",text:"Treasure counts only after the bot reaches the exit."},
    {number:"RULE 03",title:"Budget energy",text:"Normal: 1 쨌 Mud: 4 쨌 Water: 7 쨌 Collect: 1"}
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
      focus: "DFS/BFS parent tree 쨌 Provided maps",
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
      focus: "Intermediate practice 쨌 Provided scenarios",
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


