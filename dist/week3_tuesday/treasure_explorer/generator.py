"""Public generator for Week 3 practice maps. DO NOT EDIT.

The private evaluation uses THIS generator with seeds that are not published,
plus a few hand-made maps of the same size and rules. Designing for the
parameter ranges below is intended; memorising a particular seed is not.

Parameter ranges (inclusive):
    rows x cols        9..13 (odd) x 17..31 (odd)
    layout             random spanning-tree maze + 5..10 % extra openings (cycles)
    terrain            6..20 cells of mud (M, cost 4) or water (W, cost 7), 3:1
    treasures          4..8 with value 5..45, plus 0..2 decoys with value 1
    exit               a dead end far from the start (top third by distance)
    energy             d(S, E) + U(0.90, 1.60) * (energy to enter every walkable cell once)
    visibility         local, reveal_radius 1, hidden_values true, max_turns 500
"""

from __future__ import annotations

import heapq
import random

COST = {".": 1, "S": 1, "E": 1, "T": 1, "M": 4, "W": 7}


def _distances(grid: list[list[str]], start: tuple[int, int]) -> dict[tuple[int, int], int]:
    best = {start: 0}
    heap = [(0, start)]
    while heap:
        d, (r, c) = heapq.heappop(heap)
        if d > best[(r, c)]:
            continue
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nr, nc = r + dr, c + dc
            if grid[nr][nc] == "#":
                continue
            nd = d + COST[grid[nr][nc]]
            if nd < best.get((nr, nc), 10**9):
                best[(nr, nc)] = nd
                heapq.heappush(heap, (nd, (nr, nc)))
    return best


def generate(seed: int) -> dict:
    """Return a map dictionary in the same JSON format as maps/*.json."""
    rng = random.Random(seed)
    rows, cols = rng.choice((9, 11, 13)), rng.choice((17, 21, 25, 31))
    g = [["#"] * cols for _ in range(rows)]

    cells = [(r, c) for r in range(1, rows - 1, 2) for c in range(1, cols - 1, 2)]
    first = rng.choice(cells)
    g[first[0]][first[1]] = "."
    stack, seen = [first], {first}
    while stack:
        r, c = stack[-1]
        nxt = [(r + dr, c + dc, dr, dc) for dr, dc in ((2, 0), (-2, 0), (0, 2), (0, -2))
               if 0 < r + dr < rows - 1 and 0 < c + dc < cols - 1 and (r + dr, c + dc) not in seen]
        if not nxt:
            stack.pop()
            continue
        nr, nc, dr, dc = rng.choice(nxt)
        g[r + dr // 2][c + dc // 2] = "."
        g[nr][nc] = "."
        seen.add((nr, nc))
        stack.append((nr, nc))

    for _ in range(int(rows * cols * rng.uniform(0.05, 0.10))):
        r, c = rng.randrange(1, rows - 1), rng.randrange(1, cols - 1)
        if g[r][c] == "#" and ((g[r - 1][c] != "#" != g[r + 1][c]) or (g[r][c - 1] != "#" != g[r][c + 1])):
            g[r][c] = "."

    free = [(r, c) for r in range(rows) for c in range(cols) if g[r][c] == "."]
    start = rng.choice(free)
    g[start[0]][start[1]] = "S"
    dist = _distances(g, start)
    degree = lambda p: sum(g[p[0] + dr][p[1] + dc] != "#" for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)))
    ends = sorted((p for p in free if p != start and degree(p) == 1), key=lambda p: dist[p])
    far = ends[len(ends) * 2 // 3:] or sorted(free, key=lambda p: dist[p])[-3:]
    exit_pos = rng.choice(far)
    g[exit_pos[0]][exit_pos[1]] = "E"

    rest = [p for p in free if p not in (start, exit_pos)]
    rng.shuffle(rest)
    n_terrain, n_treasure, n_decoy = rng.randint(6, 20), rng.randint(4, 8), rng.randint(0, 2)
    for p in rest[:n_terrain]:
        g[p[0]][p[1]] = "W" if rng.random() < 0.25 else "M"
    spots = rest[n_terrain:n_terrain + n_treasure + n_decoy]
    treasures = []
    for i, p in enumerate(spots):
        g[p[0]][p[1]] = "T"
        treasures.append({"position": list(p), "value": 1 if i >= n_treasure else rng.randint(5, 45)})

    walk = sum(COST[t] for row in g for t in row if t != "#")
    d_exit = _distances(g, start)[exit_pos]
    return {
        "title": f"Generated practice seed {seed}",
        "energy": int(d_exit + rng.uniform(0.90, 1.60) * walk),
        "visibility": "local",
        "reveal_radius": 1,
        "hidden_values": True,
        "grid": ["".join(row) for row in g],
        "treasures": treasures,
    }
