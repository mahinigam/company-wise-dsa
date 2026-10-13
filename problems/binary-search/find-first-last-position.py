"""Find First and Last Position of Element

Difficulty: Medium
Topic: binary-search
Preparation tags (not verified question attribution): Amazon, Google, Microsoft
Source: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

Problem summary: Find the first and last index of a target in a sorted array.
Approach: Run lower-bound searches for target and target+1.
Complexity: O(log n) time and O(1) space.
"""

def search_range(nums: list[int], target: int) -> list[int]:
    def lower_bound(value: int) -> int:
        lo, hi = 0, len(nums)
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] < value: lo = mid + 1
            else: hi = mid
        return lo
    left = lower_bound(target)
    if left == len(nums) or nums[left] != target: return [-1, -1]
    return [left, lower_bound(target + 1) - 1]

assert search_range([5, 7, 7, 8, 8, 10], 8) == [3, 4]
assert search_range([5, 7, 7, 8], 6) == [-1, -1]
assert search_range([], 0) == [-1, -1]
