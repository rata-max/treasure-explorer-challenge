// Edit this file and click "Commit changes". GitHub Pages updates automatically.
window.SITE_CONTENT = {
  semester: "Problem Solving Techniques · Fall 2026",
  badge: "WEEK 01 · 6-HOUR LAB",
  title: "Explore.",
  subtitle: "Collect. Return.",
  description: "Plan under partial information. Collect valuable treasure and reach the exit before energy runs out.",
  labHours: "6H", initialEnergy: "100", submission: "student/agent.py",
  pythonVersion: "Python 3.11+",
  command: "python -m treasure_explorer --map maps/example_easy.json --agent student/agent.py",
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
    ["25","Performance","Hidden score and code quality"],
    ["10","Design note","Complexity and failure analysis"]
  ],
  weeks: [
    {
      number: "01", title: "VALUE-AWARE TREASURE HUNTER",
      tagline: "Evaluate treasures, manage energy, and replan online.",
      focus: "Online reward-cost decision making",
      objectives: ["Score each treasure using reward, travel cost, and return cost.", "Replan when value or terrain is revealed.", "Reach the exit on every public map."],
      deliverables: ["student/agent.py", "One-page design note", "Public-map result table"]
    },
    {
      number: "02", title: "RISK-AWARE ONLINE PLANNER",
      tagline: "Balance expected reward against uncertain travel costs.",
      focus: "Planning under uncertainty",
      objectives: ["Model expected and worst-case terrain costs.", "Adjust risk using remaining energy.", "Choose and abandon multi-treasure plans online."],
      deliverables: ["student/agent.py", "Risk model description", "Week 1 comparison"]
    },
    {
      number: "03", title: "ROBUST EXPLORER CHAMPIONSHIP",
      tagline: "Generalize across unseen maps, costs, and treasure values.",
      focus: "Hidden-map robustness",
      objectives: ["Generalize without map-specific hardcoding.", "Improve average score, exit rate, and worst-case behavior.", "Keep every decision within the runtime limit."],
      deliverables: ["Final student/agent.py", "Two-page final report", "Failure and ablation analysis"]
    }
  ],
  submissionRules: [
    "Modify and submit student/agent.py only.",
    "Do not modify the engine, maps, tests, runner, or configuration files.",
    "The final agent is evaluated on unseen hidden maps and seeds.",
    "Public-map scores are for development and do not guarantee the final score.",
    "The agent must not access files, networks, subprocesses, or external packages."
  ],
  integrityRules: [
    "Do not copy or share another student's agent code.",
    "Do not publish solution code in a public repository before grading ends.",
    "Do not identify hidden maps or seeds through hardcoding or side channels.",
    "Declare external code, references, and permitted AI assistance in the report."
  ]
};
