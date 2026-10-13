"""Rotate Function

Difficulty: Medium
Topic: arrays
Preparation tags (not verified question attribution): Google, Amazon, Adobe
Source: https://leetcode.com/problems/rotate-function/

Problem summary: Maximize F(k)=sum(i * rotated[i]) over all right rotations.
Approach: Derive F(k) from F(k-1) using total sum and the value rotated to the front.
Complexity: O(n) time and O(1) space.
"""

def max_rotate_function(nums: list[int]) -> int:
    if not nums: return 0
    total = sum(nums)
    current = sum(i * value for i, value in enumerate(nums))
    best = current
    n = len(nums)
    for k in range(n - 1, 0, -1):
        current = current + total - n * nums[k]
        best = max(best, current)
    return best

assert max_rotate_function([4,3,2,6]) == 26
assert max_rotate_function([100]) == 0
assert max_rotate_function([]) == 0
