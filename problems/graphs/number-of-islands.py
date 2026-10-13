"""Number of Islands

Difficulty: Medium
Topic: graphs
Preparation tags (not verified question attribution): Amazon, Microsoft, Google, Meta
Source: https://leetcode.com/problems/number-of-islands/

Problem summary: Count connected components of land cells in a grid.
Approach: Start DFS at each unseen land cell and mark its full four-directional component.
Complexity: O(rows×cols) time and O(rows×cols) worst-case stack/visited space.
"""

def num_islands(grid: list[list[str]]) -> int:
    if not grid or not grid[0]: return 0
    rows, cols = len(grid), len(grid[0])
    seen, count = set(), 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != "1" or (r, c) in seen: continue
            count += 1; stack = [(r, c)]; seen.add((r, c))
            while stack:
                x, y = stack.pop()
                for nx, ny in ((x-1,y), (x+1,y), (x,y-1), (x,y+1)):
                    if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == "1" and (nx, ny) not in seen:
                        seen.add((nx, ny)); stack.append((nx, ny))
    return count

assert num_islands([list("11000"), list("11000"), list("00100"), list("00011")]) == 3
assert num_islands([]) == 0
