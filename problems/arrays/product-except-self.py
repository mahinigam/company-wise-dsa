"""Product of Array Except Self

Difficulty: Medium
Topic: arrays
Preparation tags (not verified question attribution): Microsoft, Amazon, Meta, Uber
Source: https://leetcode.com/problems/product-of-array-except-self/

Problem summary: Build an output where each position is the product of all other values, without division.
Approach: Use a left-product pass followed by a right-product pass.
Complexity: O(n) time and O(1) extra space excluding output.
"""

def product_except_self(nums: list[int]) -> list[int]:
    result = [1] * len(nums)
    prefix = 1
    for i, value in enumerate(nums):
        result[i] = prefix
        prefix *= value
    suffix = 1
    for i in range(len(nums) - 1, -1, -1):
        result[i] *= suffix
        suffix *= nums[i]
    return result


assert product_except_self([1, 2, 3, 4]) == [24, 12, 8, 6]
assert product_except_self([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]
