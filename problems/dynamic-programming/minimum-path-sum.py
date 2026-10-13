"""Minimum Path Sum

Difficulty: Medium
Topic: dynamic-programming
Preparation tags (not verified question attribution): Amazon, Google, Microsoft
Source: https://leetcode.com/problems/minimum-path-sum/

Problem summary: Find the minimum sum path from the top-left to bottom-right, moving only right or down.
Approach: Update a single DP row with the smaller of the path from above or left.
Complexity: O(rows×cols) time and O(cols) space.
"""

def min_path_sum(grid: list[list[int]]) -> int:
    if not grid or not grid[0]: return 0
    cols = len(grid[0]); dp = [float("inf")] * (cols + 1); dp[1] = 0
    for row in grid:
        for c, value in enumerate(row, 1):
            dp[c] = value + min(dp[c], dp[c - 1])
    return int(dp[cols])

assert min_path_sum([[1,3,1],[1,5,1],[4,2,1]]) == 7
assert min_path_sum([[1,2,3],[4,5,6]]) == 12
assert min_path_sum([]) == 0
