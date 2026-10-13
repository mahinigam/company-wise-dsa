"""Maximum Product Subarray

Difficulty: Medium
Topic: arrays
Preparation tags (not verified question attribution): Amazon, Microsoft, Google
Source: https://leetcode.com/problems/maximum-product-subarray/

Problem summary: Find the maximum product of a contiguous non-empty subarray.
Approach: Track both minimum and maximum products ending at the current position because negatives can swap roles.
Complexity: O(n) time and O(1) extra space.
"""

def max_product(nums: list[int]) -> int:
    if not nums:
        raise ValueError("nums must be non-empty")
    high = low = best = nums[0]
    for value in nums[1:]:
        if value < 0:
            high, low = low, high
        high = max(value, high * value)
        low = min(value, low * value)
        best = max(best, high)
    return best


assert max_product([2, 3, -2, 4]) == 6
assert max_product([-2, 0, -1]) == 0
assert max_product([-2, 3, -4]) == 24
