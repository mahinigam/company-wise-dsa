"""House Robber

Difficulty: Medium
Topic: dynamic-programming
Preparation tags (not verified question attribution): Amazon, Google, Target
Source: https://leetcode.com/problems/house-robber/

Problem summary: Maximize stolen value without taking adjacent houses.
Approach: At each house choose between the previous best and the best two houses back plus current value.
Complexity: O(n) time and O(1) space.
"""

def rob(nums: list[int]) -> int:
    two_back = one_back = 0
    for value in nums:
        two_back, one_back = one_back, max(one_back, two_back + value)
    return one_back

assert rob([1, 2, 3, 1]) == 4
assert rob([2, 7, 9, 3, 1]) == 12
assert rob([]) == 0
