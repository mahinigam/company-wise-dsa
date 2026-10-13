"""Unique Paths

Difficulty: Medium
Topic: dynamic-programming
Preparation tags (not verified question attribution): Google, Amazon, Adobe
Source: https://leetcode.com/problems/unique-paths/

Problem summary: Count paths from the top-left to bottom-right of an m×n grid using only right and down moves.
Approach: One-dimensional DP accumulates ways from above and left.
Complexity: O(mn) time and O(n) space.
"""

def unique_paths(m: int, n: int) -> int:
    if m <= 0 or n <= 0: return 0
    dp = [1] * n
    for _ in range(1, m):
        for c in range(1, n): dp[c] += dp[c - 1]
    return dp[-1]

assert unique_paths(3, 7) == 28
assert unique_paths(3, 2) == 3
assert unique_paths(0, 2) == 0
