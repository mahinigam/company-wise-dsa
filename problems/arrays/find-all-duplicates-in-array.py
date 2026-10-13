"""Find All Duplicates in an Array

Difficulty: Medium
Topic: arrays
Preparation tags (not verified question attribution): Amazon, Google, Uber
Source: https://leetcode.com/problems/find-all-duplicates-in-an-array/

Problem summary: Return values appearing twice in an array where values are in 1..n.
Approach: Use each value's indexed position as a sign marker to detect a prior occurrence.
Complexity: O(n) time and O(1) extra space excluding output; mutates the array.
"""

def find_duplicates(nums: list[int]) -> list[int]:
    out = []
    for value in nums:
        index = abs(value) - 1
        if nums[index] < 0: out.append(abs(value))
        else: nums[index] = -nums[index]
    return out

assert find_duplicates([4,3,2,7,8,2,3,1]) == [2,3]
assert find_duplicates([1,1,2]) == [1]
assert find_duplicates([1]) == []
