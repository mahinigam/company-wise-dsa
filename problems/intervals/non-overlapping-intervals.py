"""Non-overlapping Intervals

Difficulty: Medium
Topic: intervals
Preparation tags (not verified question attribution): Google, Amazon, Uber
Source: https://leetcode.com/problems/non-overlapping-intervals/

Problem summary: Remove the minimum number of intervals to eliminate all overlaps.
Approach: Greedily keep the interval with the earliest end whenever intervals overlap.
Complexity: O(n log n) time and O(1) extra space.
"""

def erase_overlap_intervals(intervals: list[list[int]]) -> int:
    intervals.sort(key=lambda interval: interval[1])
    removed = 0
    end = float("-inf")
    for start, finish in intervals:
        if start < end: removed += 1
        else: end = finish
    return removed

assert erase_overlap_intervals([[1,2],[2,3],[3,4],[1,3]]) == 1
assert erase_overlap_intervals([[1,2],[1,2],[1,2]]) == 2
assert erase_overlap_intervals([]) == 0
