"""First Missing Positive

Difficulty: Hard
Topic: arrays
Preparation tags (not verified question attribution): Google, Amazon, Meta
Source: https://leetcode.com/problems/first-missing-positive/

Problem summary: Find the smallest positive integer missing from an unsorted array.
Approach: Place each value x in slot x-1 when x is in 1..n, then find the first mismatch.
Complexity: O(n) time and O(1) auxiliary space.
"""

def first_missing_positive(nums: list[int]) -> int:
    n = len(nums)
    for i in range(n):
        while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
            target = nums[i] - 1
            nums[i], nums[target] = nums[target], nums[i]
    for i, value in enumerate(nums):
        if value != i + 1: return i + 1
    return n + 1

assert first_missing_positive([1,2,0]) == 3
assert first_missing_positive([3,4,-1,1]) == 2
assert first_missing_positive([7,8,9,11,12]) == 1
