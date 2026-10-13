"""Coin Change

Difficulty: Medium
Topic: dynamic-programming
Preparation tags (not verified question attribution): Amazon, Microsoft, Google
Source: https://leetcode.com/problems/coin-change/

Problem summary: Find the fewest coins required to make amount, or -1 if impossible.
Approach: Bottom-up DP sets each amount to one plus the best predecessor amount for each coin.
Complexity: O(amount × number of coins) time and O(amount) space.
"""

def coin_change(coins: list[int], amount: int) -> int:
    dp = [amount + 1] * (amount + 1); dp[0] = 0
    for total in range(1, amount + 1):
        for coin in coins:
            if coin <= total: dp[total] = min(dp[total], dp[total - coin] + 1)
    return -1 if dp[amount] == amount + 1 else dp[amount]

assert coin_change([1, 2, 5], 11) == 3
assert coin_change([2], 3) == -1
assert coin_change([1], 0) == 0
