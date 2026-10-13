"""Summary Ranges

Difficulty: Easy
Topic: arrays
Preparation tags (not verified question attribution): Microsoft, Amazon, Adobe
Source: https://leetcode.com/problems/summary-ranges/

Problem summary: Summarize sorted unique integers into ranges of consecutive values.
Approach: Walk each maximal consecutive run and format a point or start->end interval.
Complexity: O(n) time and O(n) output space.
"""

def summary_ranges(nums: list[int]) -> list[str]:
    out = []; i = 0
    while i < len(nums):
        start = nums[i]
        while i + 1 < len(nums) and nums[i + 1] == nums[i] + 1: i += 1
        out.append(str(start) if start == nums[i] else f"{start}->{nums[i]}")
        i += 1
    return out

assert summary_ranges([0,1,2,4,5,7]) == ["0->2","4->5","7"]
assert summary_ranges([0,2,3,4,6,8,9]) == ["0","2->4","6","8->9"]
assert summary_ranges([]) == []
