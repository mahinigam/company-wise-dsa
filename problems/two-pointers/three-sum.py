"""3Sum

Difficulty: Medium
Topic: two-pointers
Preparation tags (not verified question attribution): Meta, Google, Amazon, Uber
Source: https://leetcode.com/problems/3sum/

Problem summary: Return unique triplets whose values sum to zero.
Approach: Sort, fix one value, then scan the remainder with two pointers while skipping duplicates.
Complexity: O(n²) time, O(1) auxiliary space excluding output.
"""

def three_sum(nums: list[int]) -> list[list[int]]:
    nums.sort()
    out = []
    for i, x in enumerate(nums):
        if i and x == nums[i - 1]: continue
        left, right = i + 1, len(nums) - 1
        while left < right:
            total = x + nums[left] + nums[right]
            if total < 0: left += 1
            elif total > 0: right -= 1
            else:
                out.append([x, nums[left], nums[right]])
                left += 1; right -= 1
                while left < right and nums[left] == nums[left - 1]: left += 1
                while left < right and nums[right] == nums[right + 1]: right -= 1
    return out

assert three_sum([-1, 0, 1, 2, -1, -4]) == [[-1, -1, 2], [-1, 0, 1]]
assert three_sum([0, 1, 1]) == []
assert three_sum([0, 0, 0]) == [[0, 0, 0]]
