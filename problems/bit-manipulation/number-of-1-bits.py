"""Number of 1 Bits

Difficulty: Easy
Topic: bit-manipulation
Preparation tags (not verified question attribution): Google, Microsoft, Amazon
Source: https://leetcode.com/problems/number-of-1-bits/

Problem summary: Count set bits in a non-negative integer.
Approach: Repeatedly clear the least significant set bit with n &= n-1.
Complexity: O(number of set bits) time and O(1) space.
"""

def hamming_weight(n: int) -> int:
    count = 0
    while n:
        n &= n - 1
        count += 1
    return count

assert hamming_weight(11) == 3
assert hamming_weight(128) == 1
assert hamming_weight(0) == 0
