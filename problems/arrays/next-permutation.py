"""Next Permutation

Difficulty: Medium
Topic: arrays
Preparation tags (not verified question attribution): Google, Amazon, Microsoft
Source: https://leetcode.com/problems/next-permutation/

Problem summary: Transform a sequence to its next lexicographically greater permutation in place.
Approach: Find the rightmost ascent, swap pivot with the next larger value, then reverse suffix.
Complexity: O(n) time, O(1) space.
"""

def next_permutation(nums: list[int]) -> None:
    i = len(nums) - 2
    while i >= 0 and nums[i] >= nums[i + 1]: i -= 1
    if i >= 0:
        j = len(nums) - 1
        while nums[j] <= nums[i]: j -= 1
        nums[i], nums[j] = nums[j], nums[i]
    left, right = i + 1, len(nums) - 1
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1; right -= 1

v = [1, 2, 3]; next_permutation(v); assert v == [1, 3, 2]
v = [3, 2, 1]; next_permutation(v); assert v == [1, 2, 3]
v = [1, 1, 5]; next_permutation(v); assert v == [1, 5, 1]
