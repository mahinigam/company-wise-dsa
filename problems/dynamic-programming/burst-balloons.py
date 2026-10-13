"""Burst Balloons

Difficulty: Hard
Topic: dynamic-programming
Preparation tags (not verified question attribution): Google, Amazon, Meta
Source: https://leetcode.com/problems/burst-balloons/

Problem summary: Maximize coins from bursting balloons, where neighbours change after every burst.
Approach: Interval DP chooses the last balloon to burst within each interval.
Complexity: O(n³) time and O(n²) space.
"""

def max_coins(nums: list[int]) -> int:
    values = [1] + nums + [1]
    n = len(nums)
    dp = [[0] * (n + 2) for _ in range(n + 2)]
    for length in range(1, n + 1):
        for left in range(1, n - length + 2):
            right = left + length - 1
            for last in range(left, right + 1):
                dp[left][right] = max(dp[left][right], values[left - 1] * values[last] * values[right + 1] + dp[left][last - 1] + dp[last + 1][right])
    return dp[1][n]

assert max_coins([3,1,5,8]) == 167
assert max_coins([1,5]) == 10
assert max_coins([]) == 0
