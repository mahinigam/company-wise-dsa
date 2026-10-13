"""House Robber II

Difficulty: Medium
Topic: dynamic-programming
Preparation tags (not verified question attribution): Amazon, Google, Meta
Source: https://leetcode.com/problems/house-robber-ii/

Problem summary: Maximize non-adjacent house value when first and last houses are adjacent.
Approach: Solve two linear robber problems, excluding first or excluding last house.
Complexity: O(n) time and O(1) space.
"""

def rob_circle(nums: list[int]) -> int:
    def linear(values):
        prev2 = prev1 = 0
        for value in values: prev2, prev1 = prev1, max(prev1, prev2 + value)
        return prev1
    if len(nums) <= 1: return max(nums, default=0)
    return max(linear(nums[:-1]), linear(nums[1:]))

assert rob_circle([2, 3, 2]) == 3
assert rob_circle([1, 2, 3, 1]) == 4
assert rob_circle([1]) == 1
