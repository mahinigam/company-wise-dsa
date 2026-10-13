"""Walls and Gates

Difficulty: Medium
Topic: graphs
Preparation tags (not verified question attribution): Amazon, Microsoft, Google
Source: https://leetcode.com/problems/walls-and-gates/

Problem summary: Fill each empty room with its distance to the nearest gate; walls remain unchanged.
Approach: Start BFS from all gates at once and assign each unvisited room its parent's distance plus one.
Complexity: O(rows×cols) time and O(rows×cols) queue space.
"""

from collections import deque

def walls_and_gates(rooms: list[list[int]]) -> None:
    if not rooms or not rooms[0]: return
    rows, cols = len(rooms), len(rooms[0])
    queue = deque((r,c) for r in range(rows) for c in range(cols) if rooms[r][c] == 0)
    inf = 2**31 - 1
    while queue:
        r, c = queue.popleft()
        for nr, nc in ((r-1,c),(r+1,c),(r,c-1),(r,c+1)):
            if 0 <= nr < rows and 0 <= nc < cols and rooms[nr][nc] == inf:
                rooms[nr][nc] = rooms[r][c] + 1; queue.append((nr,nc))

g = [[2147483647, -1, 0, 2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]
walls_and_gates(g)
assert g[0] == [3, -1, 0, 1] and g[3][2] == 3
