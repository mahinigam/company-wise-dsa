"""Best Time to Buy and Sell Stock II

Difficulty: Medium
Topic: dynamic-programming
Preparation tags (not verified question attribution): Amazon, Microsoft, Uber
Source: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

Problem summary: Maximize profit with any number of buy/sell transactions, holding at most one share at a time.
Approach: Collect every positive adjacent price increase.
Complexity: O(n) time and O(1) space.
"""

def max_profit_unlimited(prices: list[int]) -> int:
    return sum(max(0, prices[i] - prices[i - 1]) for i in range(1, len(prices)))

assert max_profit_unlimited([7,1,5,3,6,4]) == 7
assert max_profit_unlimited([1,2,3,4,5]) == 4
assert max_profit_unlimited([7,6,4,3,1]) == 0
