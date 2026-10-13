"""Minimum Interval to Include Each Query

Difficulty: Hard
Topic: heaps
Preparation tags (not verified question attribution): Google, Amazon, Meta
Source: https://leetcode.com/problems/minimum-interval-to-include-each-query/

Problem summary: For each query, return the smallest interval length that contains it, or -1.
Approach: Sort queries and interval starts; a min-heap prioritizes size while expired intervals are removed.
Complexity: O((n+q) log n) time and O(n+q) space.
"""

import heapq

def min_interval(intervals: list[list[int]], queries: list[int]) -> list[int]:
    intervals.sort()
    ordered = sorted(enumerate(queries), key=lambda pair: pair[1])
    heap = []; result = [-1] * len(queries); i = 0
    for index, query in ordered:
        while i < len(intervals) and intervals[i][0] <= query:
            left, right = intervals[i]
            heapq.heappush(heap, (right - left + 1, right)); i += 1
        while heap and heap[0][1] < query: heapq.heappop(heap)
        if heap: result[index] = heap[0][0]
    return result

assert min_interval([[1,4],[2,4],[3,6],[4,4]], [2,3,4,5]) == [3,3,1,4]
assert min_interval([[2,3],[2,5],[1,8],[20,25]], [2,19,5,22]) == [2,-1,4,6]
