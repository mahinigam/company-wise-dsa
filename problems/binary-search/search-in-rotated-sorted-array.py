"""Search in Rotated Sorted Array

Difficulty: Medium
Topic: binary-search
Preparation tags (not verified question attribution): Microsoft, Amazon, Meta
Source: https://leetcode.com/problems/search-in-rotated-sorted-array/

Problem summary: Search a target in a rotated strictly increasing array.
Approach: At each step, identify which half is sorted and keep the half that can contain target.
Complexity: O(log n) time and O(1) space.
"""

def search_rotated(nums: list[int], target: int) -> int:
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target: return mid
        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]: right = mid - 1
            else: left = mid + 1
        else:
            if nums[mid] < target <= nums[right]: left = mid + 1
            else: right = mid - 1
    return -1

assert search_rotated([4, 5, 6, 7, 0, 1, 2], 0) == 4
assert search_rotated([4, 5, 6, 7, 0, 1, 2], 3) == -1
assert search_rotated([1], 0) == -1
