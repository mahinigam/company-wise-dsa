"""Contains Duplicate

Difficulty: Easy
Topic: hashing
Preparation tags (not verified question attribution): Amazon, Microsoft, Adobe
Source: https://leetcode.com/problems/contains-duplicate/

Problem summary: Determine whether any value occurs at least twice.
Approach: Compare the array length with the number of unique values.
Complexity: O(n) expected time and O(n) space.
"""

def contains_duplicate(nums: list[int]) -> bool:
    return len(nums) != len(set(nums))


assert contains_duplicate([1, 2, 3, 1])
assert not contains_duplicate([1, 2, 3, 4])
assert contains_duplicate([0, 0])
