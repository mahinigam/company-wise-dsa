"""Maximum Subarray

Difficulty: Medium
Topic: arrays
Preparation tags (not verified question attribution): Microsoft, Amazon, Google, Adobe
Source: https://leetcode.com/problems/maximum-subarray/

Problem summary: Find the largest sum among all contiguous non-empty subarrays.
Approach: Kadane's algorithm keeps the best sum ending at the current index.
Complexity: O(n) time and O(1) extra space.
"""

def max_sub_array(nums: list[int]) -> int:
    if not nums:
        raise ValueError("nums must be non-empty")
    ending = best = nums[0]
    for value in nums[1:]:
        ending = max(value, ending + value)
        best = max(best, ending)
    return best


assert max_sub_array([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
assert max_sub_array([-3, -1, -2]) == -1
