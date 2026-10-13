"""String to Integer (atoi)

Difficulty: Medium
Topic: strings
Preparation tags (not verified question attribution): Microsoft, Amazon, Adobe
Source: https://leetcode.com/problems/string-to-integer-atoi/

Problem summary: Parse a leading signed integer after whitespace, stopping at the first non-digit and clamping to 32-bit bounds.
Approach: Skip leading spaces, read optional sign and digit run, then clamp the parsed value.
Complexity: O(n) time and O(1) space.
"""

def my_atoi(s: str) -> int:
    i, n = 0, len(s)
    while i < n and s[i].isspace(): i += 1
    sign = 1
    if i < n and s[i] in "+-":
        sign = -1 if s[i] == "-" else 1; i += 1
    value = 0
    while i < n and s[i].isdigit():
        value = value * 10 + int(s[i]); i += 1
    value *= sign
    return max(-(2**31), min(2**31 - 1, value))

assert my_atoi("42") == 42
assert my_atoi("   -42") == -42
assert my_atoi("4193 with words") == 4193
assert my_atoi("words and 987") == 0
assert my_atoi("91283472332") == 2**31 - 1
