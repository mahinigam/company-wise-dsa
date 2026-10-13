"""Integer Break

Difficulty: Medium
Topic: dynamic-programming
Preparation tags (not verified question attribution): Google, Amazon, Microsoft
Source: https://leetcode.com/problems/integer-break/

Problem summary: Split n into at least two positive integers to maximize their product.
Approach: DP tries each first split and reuses the best product for the remainder.
Complexity: O(n²) time and O(n) space.
"""

def integer_break(n: int) -> int:
    if n < 2: return 0
    dp = [0] * (n + 1); dp[1] = 1
    for total in range(2, n + 1):
        for part in range(1, total):
            dp[total] = max(dp[total], part * (total - part), part * dp[total - part])
    return dp[n]

assert integer_break(2) == 1
assert integer_break(10) == 36
assert integer_break(8) == 18
