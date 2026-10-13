"""Valid Triangle Number

Difficulty: Medium
Topic: two-pointers
Preparation tags (not verified question attribution): Amazon, Google, Target
Source: https://leetcode.com/problems/valid-triangle-number/

Problem summary: Count triplets that can form a triangle from positive side lengths.
Approach: Sort sides; fix the largest side and count valid pairs with two pointers.
Complexity: O(n²) time and O(1) extra space beyond sorting.
"""

def triangle_number(nums: list[int]) -> int:
    nums.sort(); count = 0
    for k in range(len(nums) - 1, 1, -1):
        left, right = 0, k - 1
        while left < right:
            if nums[left] + nums[right] > nums[k]:
                count += right - left
                right -= 1
            else:
                left += 1
    return count

assert triangle_number([2,2,3,4]) == 3
assert triangle_number([4,2,3,4]) == 4
assert triangle_number([1,1,3,4]) == 0
