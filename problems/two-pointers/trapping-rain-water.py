"""Trapping Rain Water

Difficulty: Hard
Topic: two-pointers
Preparation tags (not verified question attribution): Google, Amazon, Meta, Uber
Source: https://leetcode.com/problems/trapping-rain-water/

Problem summary: Compute the amount of water trapped between elevation bars.
Approach: Use two pointers and maintain the tallest boundary seen from each side.
Complexity: O(n) time, O(1) space.
"""

def trap(height: list[int]) -> int:
    left, right = 0, len(height) - 1
    left_max = right_max = water = 0
    while left < right:
        if height[left] <= height[right]:
            left_max = max(left_max, height[left])
            water += left_max - height[left]
            left += 1
        else:
            right_max = max(right_max, height[right])
            water += right_max - height[right]
            right -= 1
    return water

assert trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6
assert trap([4, 2, 0, 3, 2, 5]) == 9
assert trap([]) == 0
