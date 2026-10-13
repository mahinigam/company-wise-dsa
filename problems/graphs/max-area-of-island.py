"""Max Area of Island

Difficulty: Medium
Topic: graphs
Preparation tags (not verified question attribution): Amazon, Microsoft, Meta
Source: https://leetcode.com/problems/max-area-of-island/

Problem summary: Return the largest four-directionally connected component of 1s.
Approach: Flood-fill each unseen island and count the cells visited.
Complexity: O(rows×cols) time and O(rows×cols) space.
"""

def max_area_of_island(grid: list[list[int]]) -> int:
    if not grid or not grid[0]: return 0
    rows, cols = len(grid), len(grid[0])
    seen, best = set(), 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != 1 or (r, c) in seen: continue
            stack = [(r, c)]; seen.add((r, c)); area = 0
            while stack:
                x, y = stack.pop(); area += 1
                for nx, ny in ((x-1,y), (x+1,y), (x,y-1), (x,y+1)):
                    if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 1 and (nx, ny) not in seen:
                        seen.add((nx, ny)); stack.append((nx, ny))
            best = max(best, area)
    return best

assert max_area_of_island([[0,0,0],[0,1,1],[0,1,1]]) == 4
assert max_area_of_island([[0,0],[0,0]]) == 0
