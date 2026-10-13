"""Decode Ways

Difficulty: Medium
Topic: dynamic-programming
Preparation tags (not verified question attribution): Google, Amazon, Microsoft
Source: https://leetcode.com/problems/decode-ways/

Problem summary: Count ways to decode a digit string where 1..26 map to letters.
Approach: DP combines valid one-digit and two-digit decodings.
Complexity: O(n) time and O(1) space.
"""

def num_decodings(s: str) -> int:
    if not s or s[0] == "0": return 0
    two_back, one_back = 1, 1
    for i in range(1, len(s)):
        current = 0
        if s[i] != "0": current += one_back
        if 10 <= int(s[i - 1:i + 1]) <= 26: current += two_back
        two_back, one_back = one_back, current
    return one_back

assert num_decodings("12") == 2
assert num_decodings("226") == 3
assert num_decodings("06") == 0
assert num_decodings("") == 0
