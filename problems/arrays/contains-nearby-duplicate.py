"""Contains Duplicate II

Difficulty: Easy
Topic: arrays
Preparation tags (not verified question attribution): Amazon, Microsoft, Meta
Source: https://leetcode.com/problems/contains-duplicate-ii/

Problem summary: Determine whether equal values occur at indices at most k apart.
Approach: Remember the most recent index for each value.
Complexity: O(n) time and O(n) space.
"""

def contains_nearby_duplicate(nums: list[int], k: int) -> bool:
    last = {}
    for i, value in enumerate(nums):
        if value in last and i - last[value] <= k: return True
        last[value] = i
    return False

assert contains_nearby_duplicate([1,2,3,1], 3)
assert contains_nearby_duplicate([1,0,1,1], 1)
assert not contains_nearby_duplicate([1,2,3,1,2,3], 2)
