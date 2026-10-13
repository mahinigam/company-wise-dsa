"""Remove Element

Difficulty: Easy
Topic: arrays
Preparation tags (not verified question attribution): Accenture, Target, Adobe
Source: https://leetcode.com/problems/remove-element/

Problem summary: Remove all occurrences of val in place and return the remaining prefix length.
Approach: Write each value unequal to val at the next destination index.
Complexity: O(n) time and O(1) space.
"""

def remove_element(nums: list[int], val: int) -> int:
    write = 0
    for value in nums:
        if value != val:
            nums[write] = value; write += 1
    return write

arr = [3,2,2,3]; length = remove_element(arr, 3)
assert length == 2 and sorted(arr[:length]) == [2,2]
arr = [0,1,2,2,3,0,4,2]; length = remove_element(arr, 2)
assert length == 5 and sorted(arr[:length]) == [0,0,1,3,4]
