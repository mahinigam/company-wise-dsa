"""Unique Paths II

Difficulty: Medium
Topic: dynamic-programming
Preparation tags (not verified question attribution): Google, Amazon, Adobe
Source: https://leetcode.com/problems/unique-paths-ii/

Problem summary: Count right/down paths through a grid while avoiding obstacle cells marked 1.
Approach: One-dimensional DP resets paths to zero at obstacles.
Complexity: O(rows×cols) time and O(cols) space.
"""

def unique_paths_with_obstacles(grid: list[list[int]]) -> int:
    if not grid or not grid[0]: return 0
    dp = [0] * len(grid[0]); dp[0] = 1
    for row in grid:
        for c, cell in enumerate(row):
            if cell == 1: dp[c] = 0
            elif c > 0: dp[c] += dp[c - 1]
    return dp[-1]

assert unique_paths_with_obstacles([[0,0,0],[0,1,0],[0,0,0]]) == 2
assert unique_paths_with_obstacles([[1]]) == 0
assert unique_paths_with_obstacles([[0,1]]) == 0
