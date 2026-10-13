"""Online Stock Span

Difficulty: Medium
Topic: stack-queue
Preparation tags (not verified question attribution): Amazon, Google, Uber
Source: https://leetcode.com/problems/online-stock-span/

Problem summary: For each incoming stock price, find consecutive prior days with price no greater than today's.
Approach: Maintain a decreasing stack of (price, span) pairs and merge lower prices.
Complexity: O(1) amortized per next call; O(n) total space.
"""

class StockSpanner:
    def __init__(self):
        self.stack = []
    def next(self, price: int) -> int:
        span = 1
        while self.stack and self.stack[-1][0] <= price:
            span += self.stack.pop()[1]
        self.stack.append((price, span))
        return span

sp = StockSpanner()
assert [sp.next(x) for x in [100,80,60,70,60,75,85]] == [1,1,1,2,1,4,6]
