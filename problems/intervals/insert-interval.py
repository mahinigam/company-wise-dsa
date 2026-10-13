"""Insert Interval

Difficulty: Medium
Topic: intervals
Preparation tags (not verified question attribution): Google, Amazon, Meta
Source: https://leetcode.com/problems/insert-interval/

Problem summary: Insert an interval into a sorted, disjoint interval list and merge overlaps.
Approach: Append intervals before the new one, merge overlaps, then append the remainder.
Complexity: O(n) time and O(n) output space.
"""

def insert_interval(intervals: list[list[int]], new_interval: list[int]) -> list[list[int]]:
    out, i = [], 0
    start, end = new_interval
    while i < len(intervals) and intervals[i][1] < start:
        out.append(intervals[i][:]); i += 1
    while i < len(intervals) and intervals[i][0] <= end:
        start = min(start, intervals[i][0]); end = max(end, intervals[i][1]); i += 1
    out.append([start, end])
    out.extend([item[:] for item in intervals[i:]])
    return out

assert insert_interval([[1,3],[6,9]], [2,5]) == [[1,5],[6,9]]
assert insert_interval([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]) == [[1,2],[3,10],[12,16]]
