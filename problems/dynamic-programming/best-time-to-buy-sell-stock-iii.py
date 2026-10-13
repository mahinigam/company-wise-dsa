"""Best Time to Buy and Sell Stock III

Difficulty: Hard
Topic: dynamic-programming
Preparation tags (not verified question attribution): Google, Amazon, Meta
Source: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/

Problem summary: Maximize stock profit using at most two transactions.
Approach: Track best states after first buy, first sell, second buy, and second sell.
Complexity: O(n) time and O(1) space.
"""

def max_profit_two_transactions(prices: list[int]) -> int:
    buy1 = buy2 = float("-inf")
    sell1 = sell2 = 0
    for price in prices:
        buy1 = max(buy1, -price)
        sell1 = max(sell1, buy1 + price)
        buy2 = max(buy2, sell1 - price)
        sell2 = max(sell2, buy2 + price)
    return sell2

assert max_profit_two_transactions([3,3,5,0,0,3,1,4]) == 6
assert max_profit_two_transactions([1,2,3,4,5]) == 4
assert max_profit_two_transactions([7,6,4,3,1]) == 0
