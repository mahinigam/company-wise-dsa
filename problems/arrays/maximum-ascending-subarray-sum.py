"""Maximum Ascending Subarray Sum

Difficulty: Easy
Topic: arrays
Preparation tags (not verified question attribution): Accenture, Target, Amazon
Source: https://leetcode.com/problems/maximum-ascending-subarray-sum/

Problem summary: Find the maximum sum of a strictly ascending contiguous subarray.
Approach: Maintain the current ascending run sum and reset it when order breaks.
Complexity: O(n) time, O(1) space.
"""

def max_ascending_sum(nums: list[int]) -> int:
    if not nums: return 0
    current = best = nums[0]
    for i in range(1, len(nums)):
        current = current + nums[i] if nums[i] > nums[i - 1] else nums[i]
        best = max(best, current)
    return best

assert max_ascending_sum([10, 20, 30, 5, 10, 50]) == 65
assert max_ascending_sum([10, 20, 30, 40, 50]) == 150
assert max_ascending_sum([12, 17, 15, 13, 10, 11, 12]) == 33
