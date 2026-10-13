"""Add Binary

Difficulty: Easy
Topic: strings
Preparation tags (not verified question attribution): Amazon, Microsoft, Adobe
Source: https://leetcode.com/problems/add-binary/

Problem summary: Add two binary strings and return the binary result.
Approach: Scan right to left with a carry, emitting each result bit.
Complexity: O(max(n,m)) time and space.
"""

def add_binary(a: str, b: str) -> str:
    i, j, carry, out = len(a) - 1, len(b) - 1, 0, []
    while i >= 0 or j >= 0 or carry:
        total = carry
        if i >= 0: total += int(a[i]); i -= 1
        if j >= 0: total += int(b[j]); j -= 1
        out.append(str(total % 2)); carry = total // 2
    return "".join(reversed(out))

assert add_binary("11", "1") == "100"
assert add_binary("1010", "1011") == "10101"
assert add_binary("0", "0") == "0
