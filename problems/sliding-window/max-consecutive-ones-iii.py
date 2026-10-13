"""Max Consecutive Ones III

Difficulty: Medium
Topic: sliding-window
Preparation tags (not verified question attribution): Google, Amazon, Meta
Source: https://leetcode.com/problems/max-consecutive-ones-iii/

Problem summary: Find the longest subarray containing at most k zeroes.
Approach: Use a sliding window and shrink while zero count exceeds k.
Complexity: O(n) time, O(1) space.
"""

def longest_ones(nums: list[int], k: int) -> int:
    left = zeros = best = 0
    for right, value in enumerate(nums):
        zeros += value == 0
        while zeros > k:
            zeros -= nums[left] == 0
            left += 1
        best = max(best, right - left + 1)
    return best

assert longest_ones([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2) == 6
assert longest_ones([0, 0, 0], 0) == 0
assert longest_ones([1, 1, 1], 0) == 3
