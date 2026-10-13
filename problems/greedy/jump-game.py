"""Jump Game

Difficulty: Medium
Topic: greedy
Preparation tags (not verified question attribution): Amazon, Microsoft, Meta
Source: https://leetcode.com/problems/jump-game/

Problem summary: Determine whether the last index is reachable when each value is a maximum forward jump.
Approach: Track the farthest reachable index and fail if the scan passes it.
Complexity: O(n) time, O(1) space.
"""

def can_jump(nums: list[int]) -> bool:
    farthest = 0
    for i, jump in enumerate(nums):
        if i > farthest: return False
        farthest = max(farthest, i + jump)
        if farthest >= len(nums) - 1: return True
    return len(nums) <= 1

assert can_jump([2, 3, 1, 1, 4])
assert not can_jump([3, 2, 1, 0, 4])
assert can_jump([0])
