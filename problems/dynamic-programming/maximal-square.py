"""Maximal Square

Difficulty: Medium
Topic: dynamic-programming
Preparation tags (not verified question attribution): Amazon, Google, Microsoft
Source: https://leetcode.com/problems/maximal-square/

Problem summary: Find the area of the largest square containing only 1s in a binary matrix.
Approach: DP value at a cell is one plus the minimum of top, left, and top-left neighbours for a 1 cell.
Complexity: O(rows×cols) time and O(cols) space.
"""

def maximal_square(matrix: list[list[str]]) -> int:
    if not matrix or not matrix[0]: return 0
    cols = len(matrix[0]); dp = [0] * (cols + 1); best = 0
    for row in matrix:
        diagonal = 0
        for c, cell in enumerate(row, 1):
            above = dp[c]
            if cell == "1":
                dp[c] = 1 + min(dp[c], dp[c - 1], diagonal)
                best = max(best, dp[c])
            else: dp[c] = 0
            diagonal = above
    return best * best

assert maximal_square([list("10100"),list("10111"),list("11111"),list("10010")]) == 4
assert maximal_square([list("0")]) == 0
