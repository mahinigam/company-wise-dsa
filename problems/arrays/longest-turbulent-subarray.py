"""Longest Turbulent Subarray

Difficulty: Medium
Topic: arrays
Preparation tags (not verified question attribution): Amazon, Google, Meta
Source: https://leetcode.com/problems/longest-turbulent-subarray/

Problem summary: Find the longest contiguous subarray whose adjacent comparisons alternate between greater and less.
Approach: Maintain lengths ending in an up-step and a down-step.
Complexity: O(n) time and O(1) space.
"""

def max_turbulence_size(arr: list[int]) -> int:
    if not arr: return 0
    up = down = best = 1
    for i in range(1, len(arr)):
        if arr[i] > arr[i - 1]: up, down = down + 1, 1
        elif arr[i] < arr[i - 1]: down, up = up + 1, 1
        else: up = down = 1
        best = max(best, up, down)
    return best

assert max_turbulence_size([9,4,2,10,7,8,8,1,9]) == 5
assert max_turbulence_size([4,8,12,16]) == 2
assert max_turbulence_size([100]) == 1
