"""Excel Sheet Column Title

Difficulty: Easy
Topic: math
Preparation tags (not verified question attribution): Microsoft, Amazon, Adobe
Source: https://leetcode.com/problems/excel-sheet-column-title/

Problem summary: Convert a positive integer to an Excel column label.
Approach: Use 1-based base-26 conversion by subtracting one before each division.
Complexity: O(log n) time and output space.
"""

def convert_to_title(column_number: int) -> str:
    out = []
    while column_number:
        column_number -= 1
        column_number, remainder = divmod(column_number, 26)
        out.append(chr(ord("A") + remainder))
    return "".join(reversed(out))

assert convert_to_title(1) == "A"
assert convert_to_title(28) == "AB"
assert convert_to_title(701) == "ZY"
