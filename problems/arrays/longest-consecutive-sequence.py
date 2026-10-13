"""Longest Consecutive Sequence

Difficulty: Medium
Topic: arrays
Preparation tags (not verified question attribution): Google, Amazon, Meta, Uber
Source: https://leetcode.com/problems/longest-consecutive-sequence/

Problem summary: Find the longest run of consecutive integers without sorting.
Approach: Start a run only at values whose predecessor is absent from the set.
Complexity: O(n) expected time and O(n) space.
"""

def longest_consecutive(nums: list[int]) -> int:
    values = set(nums)
    best = 0
    for value in values:
        if value - 1 not in values:
            current = value
            while current in values:
                current += 1
            best = max(best, current - value)
    return best


assert longest_consecutive([100, 4, 200, 1, 3, 2]) == 4
assert longest_consecutive([]) == 0
