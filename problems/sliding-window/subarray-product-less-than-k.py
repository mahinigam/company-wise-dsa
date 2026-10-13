"""Subarray Product Less Than K

Difficulty: Medium
Topic: sliding-window
Preparation tags (not verified question attribution): Google, Amazon, Meta
Source: https://leetcode.com/problems/subarray-product-less-than-k/

Problem summary: Count non-empty contiguous subarrays with product less than k; values are positive.
Approach: Maintain a multiplicative sliding window and count all valid suffixes ending at each right index.
Complexity: O(n) time, O(1) space.
"""

def num_subarray_product_less_than_k(nums: list[int], k: int) -> int:
    if k <= 1: return 0
    product = 1
    left = answer = 0
    for right, value in enumerate(nums):
        product *= value
        while product >= k:
            product //= nums[left]
            left += 1
        answer += right - left + 1
    return answer

assert num_subarray_product_less_than_k([10, 5, 2, 6], 100) == 8
assert num_subarray_product_less_than_k([1, 2, 3], 0) == 0
assert num_subarray_product_less_than_k([1, 1, 1], 2) == 6
