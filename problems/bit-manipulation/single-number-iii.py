"""Single Number III

Difficulty: Medium
Topic: bit-manipulation
Preparation tags (not verified question attribution): Google, Microsoft, Amazon
Source: https://leetcode.com/problems/single-number-iii/

Problem summary: Find the two values appearing once when every other value appears twice.
Approach: XOR all values, split by one set bit of the XOR result, and XOR each group separately.
Complexity: O(n) time and O(1) space.
"""

def single_number_iii(nums: list[int]) -> list[int]:
    combined = 0
    for value in nums: combined ^= value
    bit = combined & -combined
    first = second = 0
    for value in nums:
        if value & bit: first ^= value
        else: second ^= value
    return sorted([first, second])

assert single_number_iii([1,2,1,3,2,5]) == [3,5]
assert single_number_iii([-1,0]) == [-1,0]
assert single_number_iii([0,1]) == [0,1]
