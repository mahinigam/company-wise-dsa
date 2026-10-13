"""Sum of Two Integers Without +

Difficulty: Medium
Topic: bit-manipulation
Preparation tags (not verified question attribution): Google, Amazon, Meta
Source: https://leetcode.com/problems/sum-of-two-integers/

Problem summary: Add two signed 32-bit integers without using + or -.
Approach: XOR calculates sum bits without carry; AND plus left shift calculates carry. Mask to 32 bits.
Complexity: O(1) time with fixed 32-bit width, O(1) space.
"""

def get_sum(a: int, b: int) -> int:
    mask = 0xFFFFFFFF
    max_int = 0x7FFFFFFF
    a &= mask; b &= mask
    while b:
        a, b = (a ^ b) & mask, ((a & b) << 1) & mask
    return a if a <= max_int else ~(a ^ mask)

assert get_sum(1, 2) == 3
assert get_sum(2, 3) == 5
assert get_sum(-2, 3) == 1
