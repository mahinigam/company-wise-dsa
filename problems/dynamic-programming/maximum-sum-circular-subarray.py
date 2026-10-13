"""Maximum Sum Circular Subarray

Difficulty: Medium
Topic: dynamic-programming
Preparation tags (not verified question attribution): Google, Amazon, Microsoft
Source: https://leetcode.com/problems/maximum-sum-circular-subarray/

Problem summary: Find the maximum non-empty subarray sum in a circular array.
Approach: Compare normal Kadane's maximum with total sum minus the minimum subarray; handle all-negative arrays separately.
Complexity: O(n) time and O(1) space.
"""

def max_subarray_sum_circular(nums: list[int]) -> int:
    total = sum(nums)
    max_ending = max_sum = nums[0]
    min_ending = min_sum = nums[0]
    for value in nums[1:]:
        max_ending = max(value, max_ending + value)
        max_sum = max(max_sum, max_ending)
        min_ending = min(value, min_ending + value)
        min_sum = min(min_sum, min_ending)
    return max_sum if max_sum < 0 else max(max_sum, total - min_sum)

assert max_subarray_sum_circular([1,-2,3,-2]) == 3
assert max_subarray_sum_circular([5,-3,5]) == 10
assert max_subarray_sum_circular([-3,-2,-3]) == -2
