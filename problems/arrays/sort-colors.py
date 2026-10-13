"""Sort Colors

Difficulty: Medium
Topic: arrays
Preparation tags (not verified question attribution): Microsoft, Amazon, Meta
Source: https://leetcode.com/problems/sort-colors/

Problem summary: Sort an array containing only 0, 1, and 2 in place.
Approach: Use the Dutch-national-flag algorithm with low, current, and high pointers.
Complexity: O(n) time, O(1) space.
"""

def sort_colors(nums: list[int]) -> None:
    low = current = 0
    high = len(nums) - 1
    while current <= high:
        if nums[current] == 0:
            nums[low], nums[current] = nums[current], nums[low]
            low += 1; current += 1
        elif nums[current] == 1:
            current += 1
        else:
            nums[current], nums[high] = nums[high], nums[current]
            high -= 1

values = [2, 0, 2, 1, 1, 0]; sort_colors(values); assert values == [0, 0, 1, 1, 2, 2]
values = [0]; sort_colors(values); assert values == [0]
