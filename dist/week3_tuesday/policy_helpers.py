"""Provided helpers for the Week 3 final. DO NOT EDIT OR SUBMIT THIS FILE."""

from __future__ import annotations

from dataclasses import dataclass
from heapq import heappop, heappush
from typing import Iterable, Iterator

from treasure_explorer.model import Action, Observation


MOVES = (
    (Action.MOVE_UP, -1, 0),
    (Action.MOVE_DOWN, 1, 0),
    (Action.MOVE_LEFT, 0, -1),
    (Action.MOVE_RIGHT, 0, 1),
)
# Energy charged when ENTERING a tile: normal/start/exit/treasure 1, mud 4, water 7.
TERRAIN_COST = {".": 1, "S": 1, "E": 1, "T": 1, "M": 4, "W": 7}

Position = tuple[int, int]


@dataclass(frozen=True)
class Option:
    """One place the agent could head for next. Built by the fixed agent.py.

    kind            "frontier": a known walkable cell next to at least one "?"
                    "treasure": a seen, uncollected treasure
    position        grid cell of the option
    cost_to         energy from the current cell to ``position`` through
                    KNOWN cells, never crossing E
    cost_to_exit    energy from ``position`` to E through known cells, or None
                    while E is unseen (or not yet reachable through known cells)
    unknown_nearby  number of "?" cells within Manhattan distance 2 of
                    ``position`` (a rough "how much could I learn there")
    value           treasure value if already revealed, None if still hidden
                    (always None for frontiers)
    """

    kind: str
    position: Position
    cost_to: int
    cost_to_exit: int | None
    unknown_nearby: int
    value: int | None = None


def in_bounds(grid: tuple[str, ...], position: Position) -> bool:
    row, col = position
    return 0 <= row < len(grid) and 0 <= col < len(grid[0])


def known_neighbors(
    obs: Observation,
    position: Position,
    forbidden: Iterable[Position] = (),
) -> Iterator[tuple[Position, Action, int]]:
    """Yield ``(next_cell, action, entry_cost)``; skips walls, ``?`` and ``forbidden``."""
    blocked = set(forbidden)
    for action, dr, dc in MOVES:
        nxt = position[0] + dr, position[1] + dc
        if not in_bounds(obs.grid, nxt) or nxt in blocked:
            continue
        tile = obs.grid[nxt[0]][nxt[1]]
        if tile in TERRAIN_COST:
            yield nxt, action, TERRAIN_COST[tile]


def dijkstra_all(
    obs: Observation,
    start: Position,
    forbidden: Iterable[Position] = (),
) -> tuple[dict[Position, int], dict[Position, tuple[Position, Action]]]:
    """Single-source Dijkstra over known cells: (cost, parent) for every reachable cell."""
    blocked = tuple(forbidden)
    best = {start: 0}
    parent: dict[Position, tuple[Position, Action]] = {}
    heap = [(0, start)]
    while heap:
        cost, cell = heappop(heap)
        if cost > best[cell]:
            continue
        for nxt, action, step in known_neighbors(obs, cell, blocked):
            new = cost + step
            if nxt not in best or new < best[nxt]:
                best[nxt] = new
                parent[nxt] = (cell, action)
                heappush(heap, (new, nxt))
    return best, parent


def costs_to(obs: Observation, goal: Position) -> dict[Position, int]:
    """Energy from EVERY known cell to ``goal`` in one pass (reverse Dijkstra).

    Entering cell v costs TERRAIN_COST[v], so walking the reverse edge v -> u
    costs the tile of v. ``goal`` itself is never passed through.
    """
    best = {goal: 0}
    heap = [(0, goal)]
    while heap:
        cost, cell = heappop(heap)
        if cost > best[cell]:
            continue
        step = TERRAIN_COST[obs.grid[cell[0]][cell[1]]]
        for prev, _, _ in known_neighbors(obs, cell):
            new = cost + step
            if prev not in best or new < best[prev]:
                best[prev] = new
                heappush(heap, (new, prev))
    return best


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
    best, parent = dijkstra_all(obs, start, forbidden)
    if goal not in best:
        return None, None
    route: list[Action] = []
    cell = goal
    while cell != start:
        cell, action = parent[cell]
        route.append(action)
    route.reverse()
    return route, best[goal]


def exit_cost(obs: Observation, start: Position | None = None) -> int | None:
    """Known energy from ``start`` (default: current cell) to E, or None."""
    return dijkstra_path(obs, obs.position if start is None else start, obs.exit_position)[1]


def known_frontiers(obs: Observation) -> list[Position]:
    """Known walkable cells adjacent to at least one unknown cell."""
    result = []
    for row, line in enumerate(obs.grid):
        for col, tile in enumerate(line):
            if tile not in TERRAIN_COST:
                continue
            if any(
                in_bounds(obs.grid, (row + dr, col + dc))
                and obs.grid[row + dr][col + dc] == "?"
                for _, dr, dc in MOVES
            ):
                result.append((row, col))
    return result


def unknown_nearby(obs: Observation, position: Position, radius: int = 2) -> int:
    r0, c0 = position
    return sum(
        1
        for r in range(max(0, r0 - radius), min(len(obs.grid), r0 + radius + 1))
        for c in range(max(0, c0 - radius), min(len(obs.grid[0]), c0 + radius + 1))
        if abs(r - r0) + abs(c - c0) <= radius and obs.grid[r][c] == "?"
    )


def safe_known_move(obs: Observation) -> Action:
    """Deterministic last resort: an affordable known move, else MOVE_RIGHT."""
    for _, action, cost in known_neighbors(obs, obs.position):
        if cost <= obs.energy:
            return action
    return Action.MOVE_RIGHT
