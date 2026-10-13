"""Sort Array By Parity

Difficulty: Easy
Topic: arrays
Preparation tags (not verified question attribution): Amazon, Adobe, Target
Source: https://leetcode.com/problems/sort-array-by-parity/

Problem summary: Move even integers before odd integers; order within each group does not matter.
Approach: Use two pointers to swap an odd value on the left with an even value on the right.
Complexity: O(n) time and O(1) extra space.
"""

def sort_array_by_parity(nums: list[int]) -> list[int]:
    left, right = 0, len(nums) - 1
    while left < right:
        if nums[left] % 2 == 0: left += 1
        elif nums[right] % 2 == 1: right -= 1
        else:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1; right -= 1
    return nums

result = sort_array_by_parity([3,1,2,4])
assert all(x % 2 == 0 for x in result[:2]) and all(x % 2 == 1 for x in result[2:])
assert sort_array_by_parity([]) == []
