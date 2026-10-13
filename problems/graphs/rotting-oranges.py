"""Rotting Oranges

Difficulty: Medium
Topic: graphs
Preparation tags (not verified question attribution): Amazon, Microsoft, Uber
Source: https://leetcode.com/problems/rotting-oranges/

Problem summary: Return minutes until all reachable fresh oranges rot, or -1 if impossible.
Approach: Run multi-source BFS from every initially rotten orange.
Complexity: O(rows×cols) time and space.
"""

from collections import deque

def oranges_rotting(grid: list[list[int]]) -> int:
    if not grid or not grid[0]: return 0
    rows, cols = len(grid), len(grid[0])
    queue = deque((r,c) for r in range(rows) for c in range(cols) if grid[r][c] == 2)
    fresh = sum(value == 1 for row in grid for value in row)
    minutes = 0
    while queue and fresh:
        for _ in range(len(queue)):
            r, c = queue.popleft()
            for nr, nc in ((r-1,c),(r+1,c),(r,c-1),(r,c+1)):
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    grid[nr][nc] = 2; fresh -= 1; queue.append((nr,nc))
        minutes += 1
    return minutes if fresh == 0 else -1

assert oranges_rotting([[2,1,1],[1,1,0],[0,1,1]]) == 4
assert oranges_rotting([[2,1,1],[0,1,1],[1,0,1]]) == -1
assert oranges_rotting([[0,2]]) == 0
