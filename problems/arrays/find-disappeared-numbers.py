"""Find All Numbers Disappeared in an Array

Difficulty: Easy
Topic: arrays
Preparation tags (not verified question attribution): Amazon, Microsoft, Uber
Source: https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/

Problem summary: Return values in 1..n that do not occur in the array.
Approach: Build the set of present values and enumerate missing values.
Complexity: O(n) time and O(n) auxiliary space.
"""

def find_disappeared_numbers(nums: list[int]) -> list[int]:
    present = set(nums)
    return [value for value in range(1, len(nums) + 1) if value not in present]


assert find_disappeared_numbers([4, 3, 2, 7, 8, 2, 3, 1]) == [5, 6]
assert find_disappeared_numbers([1, 1]) == [2]
