"""Search Insert Position

Difficulty: Easy
Topic: binary-search
Preparation tags (not verified question attribution): Microsoft, Amazon, Adobe
Source: https://leetcode.com/problems/search-insert-position/

Problem summary: Return the index of target or the position where it should be inserted into a sorted array.
Approach: Binary search for the first position whose value is at least target.
Complexity: O(log n) time and O(1) space.
"""

def search_insert(nums: list[int], target: int) -> int:
    left, right = 0, len(nums)
    while left < right:
        mid = (left + right) // 2
        if nums[mid] < target: left = mid + 1
        else: right = mid
    return left

assert search_insert([1, 3, 5, 6], 5) == 2
assert search_insert([1, 3, 5, 6], 2) == 1
assert search_insert([], 4) == 0
