"""Week 1 starter: tree-path baseline.

This baseline reaches the key and then the exit on the easy map. It deliberately
ignores batteries. Improve target selection so the agent also solves the longer
maps without running out of energy.
"""

from treasure_explorer.model import Action, Observation

MOVES = (
    (Action.MOVE_UP, -1, 0),
    (Action.MOVE_DOWN, 1, 0),
    (Action.MOVE_LEFT, 0, -1),
    (Action.MOVE_RIGHT, 0, 1),
)


def _tree_path(obs: Observation, goal: tuple[int, int]) -> list[Action]:
    """Return the unique start-to-goal path using a DFS parent tree."""
    start = obs.position
    stack = [start]
    parent: dict[tuple[int, int], tuple[tuple[int, int], Action] | None] = {start: None}

    while stack:
        current = stack.pop()
        if current == goal:
            break
        r, c = current
        for action, dr, dc in MOVES:
            nxt = (r + dr, c + dc)
            if nxt in parent:
                continue
            if not (0 <= nxt[0] < len(obs.grid) and 0 <= nxt[1] < len(obs.grid[0])):
                continue
            if obs.grid[nxt[0]][nxt[1]] == "#":
                continue
            parent[nxt] = (current, action)
            stack.append(nxt)

    if goal not in parent:
        return []

    reversed_actions: list[Action] = []
    cursor = goal
    while cursor != start:
        previous, action = parent[cursor]  # type: ignore[misc]
        reversed_actions.append(action)
        cursor = previous
    return list(reversed(reversed_actions))


def choose_action(obs: Observation) -> Action:
    key = next((item for item in obs.items if item.kind == "key" and not item.collected), None)
    target = key.position if key and not obs.has_key else obs.exit_position
    path = _tree_path(obs, target)
    return path[0] if path else Action.COLLECT

