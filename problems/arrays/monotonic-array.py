"""Monotonic Array

Difficulty: Easy
Topic: arrays
Preparation tags (not verified question attribution): Amazon, Adobe, Target
Source: https://leetcode.com/problems/monotonic-array/

Problem summary: Determine whether an array is entirely non-decreasing or entirely non-increasing.
Approach: Track whether any ascent and any descent occur.
Complexity: O(n) time and O(1) space.
"""

def is_monotonic(nums: list[int]) -> bool:
    nondecreasing = nonincreasing = True
    for a, b in zip(nums, nums[1:]):
        if a > b: nondecreasing = False
        if a < b: nonincreasing = False
    return nondecreasing or nonincreasing

assert is_monotonic([1,2,2,3])
assert is_monotonic([6,5,4,4])
assert not is_monotonic([1,3,2])
