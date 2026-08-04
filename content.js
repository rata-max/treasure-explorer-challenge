// Edit this file and click "Commit changes". GitHub Pages updates automatically.
window.SITE_CONTENT = {
  semester: "Problem Solving Techniques · Fall 2026",
  badge: "WEEK 01~ · 6-HOUR LAB",
  title: "Treasure Explorer.",
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
    ["1week","Route","Build and recover a path with BFS."],
    ["1week","Weight","Upgrade to Dijkstra for terrain costs."],
    ["2week","State","Track unknown, known, and collected treasure."],
    ["2week","Safety","Check the energy needed to return."],
    ["3week","Test","Run public maps and review failures."]
  ],
  rubric: [
    ["20","Safe finish","Reach the exit on every public map"],
    ["20","Pathfinding","BFS/Dijkstra and path recovery"],
    ["15","Replanning","Use the latest observation"],
    ["10","Energy check","Verify a safe return"],
    ["25","Performance","Hidden score and code quality"],
    ["10","Design note","Complexity and failure analysis"]
  ]
};
