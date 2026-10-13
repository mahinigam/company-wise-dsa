"""Shortest Path in Binary Matrix

Difficulty: Medium
Topic: graphs
Preparation tags (not verified question attribution): Google, Amazon, Meta
Source: https://leetcode.com/problems/shortest-path-in-binary-matrix/

Problem summary: Find the shortest clear path from top-left to bottom-right with eight-direction moves.
Approach: Use BFS because each move has equal cost.
Complexity: O(n²) time and O(n²) space.
"""

from collections import deque

def shortest_path_binary_matrix(grid: list[list[int]]) -> int:
    n = len(grid)
    if n == 0 or grid[0][0] or grid[n-1][n-1]: return -1
    queue = deque([(0, 0, 1)]); seen = {(0, 0)}
    directions = [(dr, dc) for dr in (-1,0,1) for dc in (-1,0,1) if (dr,dc) != (0,0)]
    while queue:
        r, c, distance = queue.popleft()
        if (r, c) == (n - 1, n - 1): return distance
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0 and (nr,nc) not in seen:
                seen.add((nr,nc)); queue.append((nr,nc,distance + 1))
    return -1

assert shortest_path_binary_matrix([[0,1],[1,0]]) == 2
assert shortest_path_binary_matrix([[0,0,0],[1,1,0],[1,1,0]]) == 4
assert shortest_path_binary_matrix([[1]]) == -1
