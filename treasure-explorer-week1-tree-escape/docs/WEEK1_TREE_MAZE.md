# Week 1 — Keyed Tree Escape

## Mission

The walkable cells form a connected tree: there is exactly one simple path
between any two cells. Collect the key (`K`) and reach the exit (`E`) before
energy reaches zero. Batteries (`B`) are collected automatically and restore
energy.

## What to implement

Edit only `student/agent.py`. `choose_action(observation)` must return one of
`MOVE_UP`, `MOVE_DOWN`, `MOVE_LEFT`, or `MOVE_RIGHT` on every turn.

Use a tree-based algorithm:

1. Traverse the map with DFS or BFS and store a parent for each visited cell.
2. Recover the unique path from the current position to an item or the exit.
3. Decide which batteries are necessary before visiting the key.
4. After collecting the key, recover a safe path to the exit.

The starter already demonstrates DFS parent construction. It solves the easy
map but deliberately ignores batteries, so it fails the longer maps.

## Symbols and items

| Symbol | Meaning |
| --- | --- |
| `#` | wall |
| `.` | walkable cell; movement costs 1 |
| `S` | start |
| `K` | key; collected automatically |
| `B` | battery; collected automatically and adds `battery_gain` energy |
| `E` | exit; ends the run only after the key is collected |
| `A` | agent, shown only by the viewer |

The observation adds `items` and `has_key`. Each item has `position`, `kind`,
and `collected` fields.

## Run and view

```bash
python -m treasure_explorer --map maps/week1_tree_easy.json --agent student/agent.py
python -m treasure_explorer --map maps/week1_tree_medium.json --agent student/agent.py --view
python -m treasure_explorer --map maps/week1_tree_hard.json --agent student/agent.py --view --delay 0.05
python -m unittest discover -s tests -v
```

## Public evaluation

- Easy: reach the key and exit using the unique tree path.
- Medium: select the battery needed for a safe route.
- Hard: select multiple useful batteries without wasting energy.
- No hidden maps are used in Week 1.

Recommended rubric: correctness 40, tree traversal and path recovery 25,
energy-aware item selection 20, code quality 10, short complexity note 5.

