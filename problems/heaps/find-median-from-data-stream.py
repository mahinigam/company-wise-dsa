"""Find Median From Data Stream

Difficulty: Hard
Topic: heaps
Preparation tags (not verified question attribution): Google, Amazon, Meta, Uber
Source: https://leetcode.com/problems/find-median-from-data-stream/

Problem summary: Support number insertion and O(1) median retrieval.
Approach: Balance a max-heap of the lower half and a min-heap of the upper half.
Complexity: O(log n) insertion, O(1) median, O(n) space.
"""

import heapq

class MedianFinder:
    def __init__(self):
        self.low, self.high = [], []
    def add_num(self, num: int) -> None:
        heapq.heappush(self.low, -num)
        heapq.heappush(self.high, -heapq.heappop(self.low))
        if len(self.high) > len(self.low): heapq.heappush(self.low, -heapq.heappop(self.high))
    def find_median(self) -> float:
        if not self.low: raise ValueError("no values")
        if len(self.low) > len(self.high): return float(-self.low[0])
        return (-self.low[0] + self.high[0]) / 2

mf = MedianFinder(); mf.add_num(1); mf.add_num(2); assert mf.find_median() == 1.5
mf.add_num(3); assert mf.find_median() == 2.0
