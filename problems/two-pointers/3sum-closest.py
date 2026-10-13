"""3Sum Closest

Difficulty: Medium
Topic: two-pointers
Preparation tags (not verified question attribution): Amazon, Google, Meta
Source: https://leetcode.com/problems/3sum-closest/

Problem summary: Find a triplet sum closest to target.
Approach: Sort, fix one value, and move two pointers while tracking the closest sum.
Complexity: O(n²) time, O(1) auxiliary space.
"""

def three_sum_closest(nums: list[int], target: int) -> int:
    if len(nums) < 3: raise ValueError("at least three values required")
    nums.sort()
    best = sum(nums[:3])
    for i in range(len(nums) - 2):
        left, right = i + 1, len(nums) - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if abs(total - target) < abs(best - target): best = total
            if total < target: left += 1
            elif total > target: right -= 1
            else: return total
    return best

assert three_sum_closest([-1, 2, 1, -4], 1) == 2
assert three_sum_closest([0, 0, 0], 1) == 0
