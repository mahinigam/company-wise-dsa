"""Reverse Bits

Difficulty: Easy
Topic: bit-manipulation
Preparation tags (not verified question attribution): Google, Microsoft, Adobe
Source: https://leetcode.com/problems/reverse-bits/

Problem summary: Reverse the bit order of a 32-bit unsigned integer.
Approach: Shift one low bit at a time into the result.
Complexity: O(32) time and O(1) space.
"""

def reverse_bits(n: int) -> int:
    result = 0
    for _ in range(32):
        result = (result << 1) | (n & 1)
        n >>= 1
    return result

assert reverse_bits(43261596) == 964176192
assert reverse_bits(0) == 0
assert reverse_bits(1) == 2**31
