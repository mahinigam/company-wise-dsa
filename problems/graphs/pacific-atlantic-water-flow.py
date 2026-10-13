"""Pacific Atlantic Water Flow

Difficulty: Medium
Topic: graphs
Preparation tags (not verified question attribution): Google, Amazon, Uber
Source: https://leetcode.com/problems/pacific-atlantic-water-flow/

Problem summary: Find cells from which water can flow to both the Pacific and Atlantic edges.
Approach: Traverse backward from each ocean: movement is allowed to equal-or-higher cells.
Complexity: O(rows×cols) time and space.
"""

from collections import deque

def pacific_atlantic(heights: list[list[int]]) -> list[list[int]]:
    if not heights or not heights[0]: return []
    rows, cols = len(heights), len(heights[0])
    def reachable(starts):
        seen = set(starts); queue = deque(starts)
        while queue:
            r, c = queue.popleft()
            for nr, nc in ((r-1,c),(r+1,c),(r,c-1),(r,c+1)):
                if 0 <= nr < rows and 0 <= nc < cols and (nr,nc) not in seen and heights[nr][nc] >= heights[r][c]:
                    seen.add((nr,nc)); queue.append((nr,nc))
        return seen
    pacific = [(r, 0) for r in range(rows)] + [(0, c) for c in range(cols)]
    atlantic = [(r, cols - 1) for r in range(rows)] + [(rows - 1, c) for c in range(cols)]
    return [list(cell) for cell in sorted(reachable(pacific) & reachable(atlantic))]

assert set(map(tuple, pacific_atlantic([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]])) >= {(0,4),(4,0),(3,0)}
assert pacific_atlantic([]) == []
