"""Rotate Array

Difficulty: Medium
Topic: arrays
Preparation tags (not verified question attribution): Microsoft, Amazon, Adobe
Source: https://leetcode.com/problems/rotate-array/

Problem summary: Rotate an array to the right by k positions in place.
Approach: Reverse the whole list, then reverse the first k values and the remainder.
Complexity: O(n) time and O(1) extra space.
"""

def rotate(nums: list[int], k: int) -> None:
    if not nums:
        return
    k %= len(nums)
    def reverse(left: int, right: int) -> None:
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
    reverse(0, len(nums) - 1)
    reverse(0, k - 1)
    reverse(k, len(nums) - 1)


values = [1, 2, 3, 4, 5, 6, 7]
rotate(values, 3)
assert values == [5, 6, 7, 1, 2, 3, 4]
values = [1, 2]
rotate(values, 4)
assert values == [1, 2]
