"""Zigzag Conversion

Difficulty: Medium
Topic: strings
Preparation tags (not verified question attribution): Amazon, Microsoft, Target
Source: https://leetcode.com/problems/zigzag-conversion/

Problem summary: Write a string in zigzag rows and read each row sequentially.
Approach: Simulate a row pointer that reverses direction at the top and bottom.
Complexity: O(n) time and O(n) space.
"""

def convert_zigzag(s: str, num_rows: int) -> str:
    if num_rows <= 1 or num_rows >= len(s): return s
    rows = [""] * num_rows; row = 0; direction = -1
    for ch in s:
        rows[row] += ch
        if row == 0 or row == num_rows - 1: direction *= -1
        row += direction
    return "".join(rows)

assert convert_zigzag("PAYPALISHIRING", 3) == "PAHNAPLSIIGYIR"
assert convert_zigzag("PAYPALISHIRING", 4) == "PINALSIGYAHRPI"
assert convert_zigzag("A", 1) == "A
