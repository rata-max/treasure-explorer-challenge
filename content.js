// Edit this file and click "Commit changes". GitHub Pages updates automatically.
window.SITE_CONTENT = {
  semester: "Problem Solving Techniques · Fall 2026",
  badge: "WEEK 01 · 6-HOUR LAB",
  title: "Explore.",
  subtitle: "Collect. Return.",
  description: "Plan under partial information. Collect valuable treasure and reach the exit before energy runs out.",
  labHours: "6H", initialEnergy: "100", submission: "student/agent.py",
  pythonVersion: "Python 3.11+",
  command: "python -m treasure_explorer --map maps/week1_tree_easy.json --agent student/agent.py --view",
  scoreFormula: "TREASURE + ENERGY LEFT - 5 × INVALID",
  noExitRule: "NO EXIT, NO SCORE",
  missionLabel: "01 / MISSION",
  missionTitle: "The best path is not visible at the start.",
  missionDescription: "Observe, estimate, plan, act, and replan when new information appears.",
  process: [["01","OBSERVE","Map · Energy"],["02","ESTIMATE","Value · Return cost"],["03","PLAN","Target · Route"],["04","ACT","One action"]],
  rules: [
    {number:"RULE 01",title:"Reveal as you move",text:"Terrain costs appear nearby. Treasure values appear on arrival."},
    {number:"RULE 02",title:"Return first",text:"Treasure counts only after the bot reaches the exit."},
    {number:"RULE 03",title:"Budget energy",text:"Normal: 1 · Mud: 4 · Water: 5 · Collect: 1"}
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
    "Modify and submit student/agent.py only.",
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
