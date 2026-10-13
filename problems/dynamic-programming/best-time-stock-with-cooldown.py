"""Best Time to Buy and Sell Stock With Cooldown

Difficulty: Medium
Topic: dynamic-programming
Preparation tags (not verified question attribution): Google, Amazon, Meta
Source: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

Problem summary: Maximize profit when selling a stock forces one day of cooldown.
Approach: Maintain hold, sold-today, and rest states across each day.
Complexity: O(n) time and O(1) space.
"""

def max_profit_cooldown(prices: list[int]) -> int:
    hold, sold, rest = float("-inf"), float("-inf"), 0
    for price in prices:
        hold, sold, rest = max(hold, rest - price), hold + price, max(rest, sold)
    return int(max(sold, rest, 0))

assert max_profit_cooldown([1,2,3,0,2]) == 3
assert max_profit_cooldown([1]) == 0
assert max_profit_cooldown([]) == 0
