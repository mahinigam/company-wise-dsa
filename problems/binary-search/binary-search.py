"""Binary Search

Difficulty: Easy
Topic: binary-search
Preparation tags (not verified question attribution): Microsoft, Amazon, Google, Accenture
Source: https://leetcode.com/problems/binary-search/

Problem summary: Return the index of target in a sorted array, or -1.
Approach: Repeatedly eliminate half the search interval.
Complexity: O(log n) time and O(1) space.
"""

def search(nums: list[int], target: int) -> int:
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target: return mid
        if nums[mid] < target: left = mid + 1
        else: right = mid - 1
    return -1

assert search([-1, 0, 3, 5, 9, 12], 9) == 4
assert search([-1, 0, 3, 5, 9, 12], 2) == -1
assert search([], 0) == -1
