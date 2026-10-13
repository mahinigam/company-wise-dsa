"""Merge Sorted Array

Difficulty: Easy
Topic: arrays
Preparation tags (not verified question attribution): Microsoft, Amazon, Adobe
Source: https://leetcode.com/problems/merge-sorted-array/

Problem summary: Merge nums2 into nums1 in ascending order, using nums1's spare capacity.
Approach: Fill from the end so unread values in nums1 are not overwritten.
Complexity: O(m + n) time and O(1) extra space.
"""

def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    i, j, write = m - 1, n - 1, m + n - 1
    while j >= 0:
        if i >= 0 and nums1[i] > nums2[j]:
            nums1[write] = nums1[i]
            i -= 1
        else:
            nums1[write] = nums2[j]
            j -= 1
        write -= 1


values = [1, 2, 3, 0, 0, 0]
merge(values, 3, [2, 5, 6], 3)
assert values == [1, 2, 2, 3, 5, 6]
values = [0]
merge(values, 0, [1], 1)
assert values == [1]
