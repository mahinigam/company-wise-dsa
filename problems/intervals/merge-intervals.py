"""Merge Intervals

Difficulty: Medium
Topic: intervals
Preparation tags (not verified question attribution): Google, Amazon, Meta, Uber
Source: https://leetcode.com/problems/merge-intervals/

Problem summary: Merge all overlapping closed intervals.
Approach: Sort by start and extend the last output interval when the next one overlaps.
Complexity: O(n log n) time and O(n) output space.
"""

def merge_intervals(intervals: list[list[int]]) -> list[list[int]]:
    if not intervals: return []
    intervals = sorted(intervals)
    out = [intervals[0][:]]
    for start, end in intervals[1:]:
        if start <= out[-1][1]: out[-1][1] = max(out[-1][1], end)
        else: out.append([start, end])
    return out

assert merge_intervals([[1,3],[2,6],[8,10],[15,18]]) == [[1,6],[8,10],[15,18]]
assert merge_intervals([[1,4],[4,5]]) == [[1,5]]
assert merge_intervals([]) == []
