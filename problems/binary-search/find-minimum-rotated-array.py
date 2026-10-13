"""Find Minimum in Rotated Sorted Array

Difficulty: Medium
Topic: binary-search
Preparation tags (not verified question attribution): Amazon, Microsoft, Google
Source: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

Problem summary: Find the minimum value in a rotated strictly increasing array.
Approach: Compare the midpoint against the right boundary to retain the half containing the minimum.
Complexity: O(log n) time and O(1) space.
"""

def find_min(nums: list[int]) -> int:
    if not nums: raise ValueError("nums must be non-empty")
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] > nums[right]: left = mid + 1
        else: right = mid
    return nums[left]

assert find_min([3, 4, 5, 1, 2]) == 1
assert find_min([4, 5, 6, 7, 0, 1, 2]) == 0
assert find_min([11, 13, 15, 17]) == 11
