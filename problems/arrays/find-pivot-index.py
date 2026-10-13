"""Find Pivot Index

Difficulty: Easy
Topic: arrays
Preparation tags (not verified question attribution): Amazon, Microsoft, Target
Source: https://leetcode.com/problems/find-pivot-index/

Problem summary: Find an index where the sums strictly to its left and right are equal.
Approach: Use a running left sum and derive the right sum from the total.
Complexity: O(n) time, O(1) space.
"""

def pivot_index(nums: list[int]) -> int:
    total, left = sum(nums), 0
    for i, value in enumerate(nums):
        if left == total - left - value: return i
        left += value
    return -1

assert pivot_index([1, 7, 3, 6, 5, 6]) == 3
assert pivot_index([1, 2, 3]) == -1
assert pivot_index([2, 1, -1]) == 0
