"""Coin Change II

Difficulty: Medium
Topic: dynamic-programming
Preparation tags (not verified question attribution): Amazon, Google, Microsoft
Source: https://leetcode.com/problems/coin-change-ii/

Problem summary: Count combinations of coins that sum to amount, assuming unlimited coins of each denomination.
Approach: Process one coin at a time and update amounts in ascending order so coin order is not counted separately.
Complexity: O(amount × number of coin types) time and O(amount) space.
"""

def change(amount: int, coins: list[int]) -> int:
    dp = [0] * (amount + 1); dp[0] = 1
    for coin in coins:
        for total in range(coin, amount + 1):
            dp[total] += dp[total - coin]
    return dp[amount]

assert change(5, [1,2,5]) == 4
assert change(3, [2]) == 0
assert change(10, [10]) == 1
