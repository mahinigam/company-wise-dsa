"""Integer to Roman

Difficulty: Medium
Topic: strings
Preparation tags (not verified question attribution): Amazon, Microsoft, Adobe
Source: https://leetcode.com/problems/integer-to-roman/

Problem summary: Convert an integer from 1 to 3999 into Roman numeral notation.
Approach: Greedily consume denomination values in descending order, including subtractive pairs.
Complexity: O(1) time for the bounded input range, O(1) space.
"""

def int_to_roman(num: int) -> str:
    values = [(1000,"M"),(900,"CM"),(500,"D"),(400,"CD"),(100,"C"),(90,"XC"),(50,"L"),(40,"XL"),(10,"X"),(9,"IX"),(5,"V"),(4,"IV"),(1,"I")]
    out = []
    for value, symbol in values:
        count, num = divmod(num, value)
        out.append(symbol * count)
    return "".join(out)

assert int_to_roman(3) == "III"
assert int_to_roman(58) == "LVIII"
assert int_to_roman(1994) == "MCMXCIV
