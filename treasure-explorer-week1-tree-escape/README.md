# Treasure Explorer Bot Challenge — Week 1 Starter

Week 1 is **Keyed Tree Escape**. The public maps are connected tree mazes.
Students use DFS/BFS parent links to collect a key, choose useful batteries,
and reach the exit before energy runs out.

```bash
python -m treasure_explorer --map maps/week1_tree_easy.json --agent student/agent.py --view
```

See `docs/WEEK1_TREE_MAZE.md` for the complete student specification.

This is the starter repository for Week 1 (6-hour hands-on session) of the Problem-Solving Techniques course. Students should, in principle, only modify `student/agent.py`.

## Quick Start

The only requirement is **Python 3.11 or higher** — no external packages needed.

```bash
python -m treasure_explorer --map maps/example_easy.json --agent student/agent.py
python -m unittest discover -s tests -v
```

Run the commands above from the repository root with no installation required. They work the same way on Windows PowerShell and macOS/Linux terminals.

## Repository Structure

- `student/agent.py`: The file students submit
- `treasure_explorer/`: Fixed game engine and runner
- `maps/`: Three public practice maps
- `tests/`: Public tests
- `docs/ASSIGNMENT_WEEK1_KO.md`: Assignment specification and time plan
- `docs/GITHUB_RELEASE_GUIDE_KO.md`: GitHub release procedure for TAs

## Example Run

```bash
python -m treasure_explorer --map maps/example_medium.json --agent student/agent.py --seed 7 --verbose
```

The JSON result printed in the last line is used for grading. `--seed` provides an interface for reproducibility of identical inputs; the Week 1 public maps are deterministic.

## Submission

Submit a single file: `student/agent.py`. File I/O, networking, process execution, and use of external packages are prohibited. See the assignment specification for detailed rules.
