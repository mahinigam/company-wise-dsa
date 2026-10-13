"""Partition Equal Subset Sum

Difficulty: Medium
Topic: dynamic-programming
Preparation tags (not verified question attribution): Amazon, Google, Meta
Source: https://leetcode.com/problems/partition-equal-subset-sum/

Problem summary: Determine whether a list can be split into two subsets with equal sums.
Approach: Reduce to finding a subset that sums to half the total and update reachable sums in descending order.
Complexity: O(n·target) time and O(target) space.
"""

def can_partition(nums: list[int]) -> bool:
    total = sum(nums)
    if total % 2: return False
    target = total // 2
    reachable = {0}
    for value in nums:
        reachable |= {x + value for x in reachable if x + value <= target}
        if target in reachable: return True
    return target == 0

assert can_partition([1,5,11,5])
assert not can_partition([1,2,3,5])
assert can_partition([0,0])
