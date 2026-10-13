"""Minimum Size Subarray Sum

Difficulty: Medium
Topic: sliding-window
Preparation tags (not verified question attribution): Amazon, Microsoft, Meta
Source: https://leetcode.com/problems/minimum-size-subarray-sum/

Problem summary: Find the shortest non-empty subarray whose sum is at least target; values are positive.
Approach: Expand the right edge and shrink from the left while the window remains valid.
Complexity: O(n) time and O(1) space.
"""

def min_sub_array_len(target: int, nums: list[int]) -> int:
    left = total = 0
    best = len(nums) + 1
    for right, value in enumerate(nums):
        total += value
        while total >= target:
            best = min(best, right - left + 1)
            total -= nums[left]; left += 1
    return 0 if best == len(nums) + 1 else best

assert min_sub_array_len(7, [2, 3, 1, 2, 4, 3]) == 2
assert min_sub_array_len(4, [1, 4, 4]) == 1
assert min_sub_array_len(11, [1, 1, 1, 1]) == 0
