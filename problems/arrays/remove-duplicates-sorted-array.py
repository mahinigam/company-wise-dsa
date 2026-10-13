"""Remove Duplicates from Sorted Array

Difficulty: Easy
Topic: arrays
Preparation tags (not verified question attribution): Amazon, Microsoft, Adobe
Source: https://leetcode.com/problems/remove-duplicates-from-sorted-array/

Problem summary: Compact a sorted array in place and return its unique-prefix length.
Approach: Use a write pointer for the last unique value.
Complexity: O(n) time and O(1) extra space.
"""

def remove_duplicates(nums: list[int]) -> int:
    if not nums:
        return 0
    write = 1
    for read in range(1, len(nums)):
        if nums[read] != nums[write - 1]:
            nums[write] = nums[read]
            write += 1
    return write


values = [1, 1, 2]
length = remove_duplicates(values)
assert length == 2 and values[:length] == [1, 2]
assert remove_duplicates([]) == 0
