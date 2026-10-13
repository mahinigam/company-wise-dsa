"""Best Time to Buy and Sell Stock

Difficulty: Easy
Topic: arrays
Preparation tags (not verified question attribution): Amazon, Microsoft, Adobe, Accenture
Source: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

Problem summary: Maximize one buy-then-sell profit from daily prices.
Approach: Track the lowest price seen so far and the best profit.
Complexity: O(n) time and O(1) extra space.
"""

def max_profit(prices: list[int]) -> int:
    lowest = float("inf")
    best = 0
    for price in prices:
        lowest = min(lowest, price)
        best = max(best, price - lowest)
    return best


assert max_profit([7, 1, 5, 3, 6, 4]) == 5
assert max_profit([7, 6, 4, 3, 1]) == 0
assert max_profit([]) == 0
