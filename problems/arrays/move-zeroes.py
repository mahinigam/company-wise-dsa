"""Move Zeroes

Difficulty: Easy
Topic: arrays
Preparation tags (not verified question attribution): Meta, Microsoft, Amazon, Accenture
Source: https://leetcode.com/problems/move-zeroes/

Problem summary: Move all zeroes to the end while preserving non-zero order in place.
Approach: Compact non-zero values at the front, then fill the remaining suffix with zeroes.
Complexity: O(n) time and O(1) extra space.
"""

def move_zeroes(nums: list[int]) -> None:
    write = 0
    for value in nums:
        if value != 0:
            nums[write] = value
            write += 1
    nums[write:] = [0] * (len(nums) - write)


values = [0, 1, 0, 3, 12]
move_zeroes(values)
assert values == [1, 3, 12, 0, 0]
values = [0, 0]
move_zeroes(values)
assert values == [0, 0]
