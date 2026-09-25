"""Provided helpers for Week 2 Thursday. DO NOT EDIT OR SUBMIT THIS FILE.

``dijkstra_path`` is a reference version of Tuesday's TODO with the same
contract. ``route_cost`` / ``route_to`` wrap it so that routes to a treasure
never cross E (entering E ends the run).
"""

from __future__ import annotations

from collections import deque
from heapq import heappop, heappush
from typing import Iterable, Iterator

from treasure_explorer.model import Action, Observation


# (action, row change, column change). Row 0 is the top row, column 0 the left.
MOVES = (
    (Action.MOVE_UP, -1, 0),
    (Action.MOVE_DOWN, 1, 0),
    (Action.MOVE_LEFT, 0, -1),
    (Action.MOVE_RIGHT, 0, 1),
)
# Energy charged when ENTERING a tile: normal/start/exit/treasure 1, mud 4, water 7.
TERRAIN_COST = {".": 1, "S": 1, "E": 1, "T": 1, "M": 4, "W": 7}

Position = tuple[int, int]


def in_bounds(grid: tuple[str, ...], position: Position) -> bool:
    row, col = position
    return 0 <= row < len(grid) and 0 <= col < len(grid[0])


def known_neighbors(
    obs: Observation,
    position: Position,
    forbidden: Iterable[Position] = (),
) -> Iterator[tuple[Position, Action, int]]:
    """Yield ``(next_cell, action, entry_cost)`` for every walkable neighbour.

    Walls ``#`` and unknown cells ``?`` are skipped, and so is every cell in
    ``forbidden`` (pass ``(obs.exit_position,)`` to keep a route off the exit).
    Neighbours are always produced in the fixed order UP, DOWN, LEFT, RIGHT.
    """
    blocked = set(forbidden)
    for action, dr, dc in MOVES:
        nxt = position[0] + dr, position[1] + dc
        if not in_bounds(obs.grid, nxt) or nxt in blocked:
            continue
        tile = obs.grid[nxt[0]][nxt[1]]
        if tile in TERRAIN_COST:
            yield nxt, action, TERRAIN_COST[tile]


def bfs_path(
    obs: Observation,
    start: Position,
    goal: Position | None,
    forbidden: Iterable[Position] = (),
) -> list[Action] | None:
    """Minimum-step route. ``[]`` if start == goal, ``None`` if unreachable."""
    if goal is None:
        return None
    if start == goal:
        return []
    parent: dict[Position, tuple[Position, Action] | None] = {start: None}
    queue = deque([start])
    blocked = tuple(forbidden)
    while queue:
        cell = queue.popleft()
        if cell == goal:
            break
        for nxt, action, _ in known_neighbors(obs, cell, blocked):
            if nxt not in parent:
                parent[nxt] = (cell, action)
                queue.append(nxt)
    if goal not in parent:
        return None
    route: list[Action] = []
    cell = goal
    while cell != start:
        prev, action = parent[cell]  # type: ignore[misc]
        route.append(action)
        cell = prev
    route.reverse()
    return route


def dijkstra_path(
    obs: Observation,
    start: Position,
    goal: Position | None,
    forbidden: Iterable[Position] = (),
) -> tuple[list[Action] | None, int | None]:
    """Minimum-energy route. ``([], 0)`` if start == goal, ``(None, None)`` if unreachable."""
    if goal is None:
        return None, None
    if start == goal:
        return [], 0
    forbidden = tuple(forbidden)
    best = {start: 0}
    parent: dict[Position, tuple[Position, Action]] = {}
    heap = [(0, start)]
    while heap:
        cost, cell = heappop(heap)
        if cost > best[cell]:
            continue  # stale entry: a cheaper cost was already recorded
        if cell == goal:
            break
        for nxt, action, step in known_neighbors(obs, cell, forbidden):
            new = cost + step
            if nxt not in best or new < best[nxt]:
                best[nxt] = new
                parent[nxt] = (cell, action)
                heappush(heap, (new, nxt))
    if goal not in best:
        return None, None
    route: list[Action] = []
    cell = goal
    while cell != start:
        cell, action = parent[cell]
        route.append(action)
    route.reverse()
    return route, best[goal]


def route_to(obs: Observation, start: Position, goal: Position | None) -> list[Action] | None:
    """Cheapest route that treats E as a wall unless E is the goal."""
    forbidden = () if goal == obs.exit_position else (obs.exit_position,)
    return dijkstra_path(obs, start, goal, forbidden)[0]


def route_cost(obs: Observation, start: Position, goal: Position | None) -> int | None:
    """Energy of ``route_to``; ``None`` if unreachable."""
    forbidden = () if goal == obs.exit_position else (obs.exit_position,)
    return dijkstra_path(obs, start, goal, forbidden)[1]


def safe_known_move(obs: Observation) -> Action:
    """Deterministic last resort; a correct policy should never need it."""
    for _, action, _ in known_neighbors(obs, obs.position):
        return action
    return Action.MOVE_RIGHT
