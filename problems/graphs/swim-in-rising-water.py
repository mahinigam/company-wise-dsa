"""Swim in Rising Water

Difficulty: Hard
Topic: graphs
Preparation tags (not verified question attribution): Google, Amazon, Meta
Source: https://leetcode.com/problems/swim-in-rising-water/

Problem summary: Find the minimum time needed to move from top-left to bottom-right when water level must be at least each visited cell's elevation.
Approach: Dijkstra uses the path cost max(previous cost, next elevation).
Complexity: O(n² log n) time and O(n²) space.
"""

import heapq

def swim_in_water(grid: list[list[int]]) -> int:
    n = len(grid)
    if n == 0: return 0
    heap = [(grid[0][0], 0, 0)]; seen = set()
    while heap:
        time, r, c = heapq.heappop(heap)
        if (r,c) in seen: continue
        seen.add((r,c))
        if (r,c) == (n-1,n-1): return time
        for nr,nc in ((r-1,c),(r+1,c),(r,c-1),(r,c+1)):
            if 0 <= nr < n and 0 <= nc < n and (nr,nc) not in seen:
                heapq.heappush(heap, (max(time, grid[nr][nc]), nr, nc))
    return -1

assert swim_in_water([[0,2],[1,3]]) == 3
assert swim_in_water([[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]) == 16
