"""4Sum

Difficulty: Medium
Topic: two-pointers
Preparation tags (not verified question attribution): Amazon, Microsoft, Meta, Google
Source: https://leetcode.com/problems/4sum/

Problem summary: Return unique quadruplets that sum to a target.
Approach: Sort, fix two indices, then solve a two-sum subproblem using two pointers.
Complexity: O(n³) time, O(1) auxiliary space excluding output.
"""

def four_sum(nums: list[int], target: int) -> list[list[int]]:
    nums.sort(); out = []; n = len(nums)
    for i in range(n - 3):
        if i and nums[i] == nums[i - 1]: continue
        for j in range(i + 1, n - 2):
            if j > i + 1 and nums[j] == nums[j - 1]: continue
            left, right = j + 1, n - 1
            while left < right:
                total = nums[i] + nums[j] + nums[left] + nums[right]
                if total < target: left += 1
                elif total > target: right -= 1
                else:
                    out.append([nums[i], nums[j], nums[left], nums[right]])
                    left += 1; right -= 1
                    while left < right and nums[left] == nums[left - 1]: left += 1
                    while left < right and nums[right] == nums[right + 1]: right -= 1
    return out

assert four_sum([1, 0, -1, 0, -2, 2], 0) == [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]
assert four_sum([], 0) == []
