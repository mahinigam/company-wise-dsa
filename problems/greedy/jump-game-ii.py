"""Jump Game II

Difficulty: Medium
Topic: greedy
Preparation tags (not verified question attribution): Amazon, Google, Meta
Source: https://leetcode.com/problems/jump-game-ii/

Problem summary: Find the minimum jumps needed to reach the last index; reachability is guaranteed.
Approach: Treat the reachable range as a BFS layer and expand it greedily.
Complexity: O(n) time, O(1) space.
"""

def jump(nums: list[int]) -> int:
    if len(nums) <= 1: return 0
    jumps = current_end = farthest = 0
    for i in range(len(nums) - 1):
        farthest = max(farthest, i + nums[i])
        if i == current_end:
            jumps += 1
            current_end = farthest
            if current_end >= len(nums) - 1: break
    return jumps

assert jump([2, 3, 1, 1, 4]) == 2
assert jump([2, 3, 0, 1, 4]) == 2
assert jump([0]) == 0
