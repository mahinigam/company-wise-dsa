"""Find Peak Element

Difficulty: Medium
Topic: binary-search
Preparation tags (not verified question attribution): Google, Amazon, Meta
Source: https://leetcode.com/problems/find-peak-element/

Problem summary: Return an index whose value is greater than its neighbours.
Approach: If the sequence rises at mid, a peak exists to the right; otherwise one exists at or to the left.
Complexity: O(log n) time and O(1) space.
"""

def find_peak_element(nums: list[int]) -> int:
    if not nums: return -1
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] < nums[mid + 1]: left = mid + 1
        else: right = mid
    return left

assert find_peak_element([1, 2, 3, 1]) == 2
assert find_peak_element([1, 2, 1, 3, 5, 6, 4]) in {1, 5}
assert find_peak_element([1]) == 0
