"""Target Sum

Difficulty: Medium
Topic: dynamic-programming
Preparation tags (not verified question attribution): Google, Amazon, Meta
Source: https://leetcode.com/problems/target-sum/

Problem summary: Count ways to assign plus/minus signs to reach a target sum.
Approach: Use a dictionary DP mapping each reachable total to its number of sign assignments.
Complexity: O(n·S) states in common bounded cases, O(S) space.
"""

def find_target_sum_ways(nums: list[int], target: int) -> int:
    ways = {0: 1}
    for value in nums:
        next_ways = {}
        for total, count in ways.items():
            next_ways[total + value] = next_ways.get(total + value, 0) + count
            next_ways[total - value] = next_ways.get(total - value, 0) + count
        ways = next_ways
    return ways.get(target, 0)

assert find_target_sum_ways([1,1,1,1,1], 3) == 5
assert find_target_sum_ways([1], 1) == 1
assert find_target_sum_ways([0,0,1], 1) == 4
