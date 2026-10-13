"""Excel Sheet Column Number

Difficulty: Easy
Topic: math
Preparation tags (not verified question attribution): Microsoft, Amazon, Adobe
Source: https://leetcode.com/problems/excel-sheet-column-number/

Problem summary: Convert an Excel column label to a 1-based integer.
Approach: Evaluate the label as base 26 with A=1 through Z=26.
Complexity: O(n) time and O(1) space.
"""

def title_to_number(column_title: str) -> int:
    result = 0
    for ch in column_title:
        result = result * 26 + ord(ch) - ord("A") + 1
    return result

assert title_to_number("A") == 1
assert title_to_number("AB") == 28
assert title_to_number("ZY") == 701
