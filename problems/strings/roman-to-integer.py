"""Roman to Integer

Difficulty: Easy
Topic: strings
Preparation tags (not verified question attribution): Amazon, Microsoft, Adobe
Source: https://leetcode.com/problems/roman-to-integer/

Problem summary: Convert a valid Roman numeral into an integer.
Approach: Subtract a symbol when it precedes a larger value; otherwise add it.
Complexity: O(n) time and O(1) space.
"""

def roman_to_int(s: str) -> int:
    values = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
    total = 0
    for i, ch in enumerate(s):
        value = values[ch]
        total += -value if i + 1 < len(s) and value < values[s[i + 1]] else value
    return total

assert roman_to_int("III") == 3
assert roman_to_int("LVIII") == 58
assert roman_to_int("MCMXCIV") == 1994
