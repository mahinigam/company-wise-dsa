"""Best Time to Buy and Sell Stock With Transaction Fee

Difficulty: Medium
Topic: dynamic-programming
Preparation tags (not verified question attribution): Amazon, Google, Uber
Source: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/

Problem summary: Maximize profit with unlimited transactions and a fixed fee for each sale.
Approach: Track the best profit while holding a share and while not holding one.
Complexity: O(n) time and O(1) space.
"""

def max_profit_with_fee(prices: list[int], fee: int) -> int:
    cash, hold = 0, float("-inf")
    for price in prices:
        cash, hold = max(cash, hold + price - fee), max(hold, cash - price)
    return cash

assert max_profit_with_fee([1,3,2,8,4,9], 2) == 8
assert max_profit_with_fee([1,3,7,5,10,3], 3) == 6
assert max_profit_with_fee([], 2) == 0
