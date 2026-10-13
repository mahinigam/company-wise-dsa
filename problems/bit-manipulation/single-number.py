"""Single Number

Difficulty: Easy
Topic: bit-manipulation
Preparation tags (not verified question attribution): Google, Microsoft, Amazon
Source: https://leetcode.com/problems/single-number/

Problem summary: Find the value occurring once when every other value occurs twice.
Approach: XOR cancels equal pairs because x XOR x is zero.
Complexity: O(n) time and O(1) extra space.
"""

def single_number(nums: list[int]) -> int:
    result = 0
    for value in nums:
        result ^= value
    return result


assert single_number([2, 2, 1]) == 1
assert single_number([4, 1, 2, 1, 2]) == 4
