"""Fraction to Recurring Decimal

Difficulty: Medium
Topic: math
Preparation tags (not verified question attribution): Google, Amazon, Uber
Source: https://leetcode.com/problems/fraction-to-recurring-decimal/

Problem summary: Convert a fraction to decimal notation, enclosing any repeating fractional part in parentheses.
Approach: Track each remainder's first output position to locate the recurring cycle.
Complexity: O(number of produced digits) time and space.
"""

def fraction_to_decimal(numerator: int, denominator: int) -> str:
    if denominator == 0: raise ZeroDivisionError
    if numerator == 0: return "0"
    sign = "-" if (numerator < 0) != (denominator < 0) else ""
    numerator, denominator = abs(numerator), abs(denominator)
    integer, remainder = divmod(numerator, denominator)
    out = sign + str(integer)
    if remainder == 0: return out
    out += "."
    seen = {}
    digits = []
    while remainder and remainder not in seen:
        seen[remainder] = len(digits)
        remainder *= 10
        digit, remainder = divmod(remainder, denominator)
        digits.append(str(digit))
    if remainder:
        i = seen[remainder]
        return out + "".join(digits[:i]) + "(" + "".join(digits[i:]) + ")"
    return out + "".join(digits)

assert fraction_to_decimal(1, 2) == "0.5"
assert fraction_to_decimal(2, 3) == "0.(6)"
assert fraction_to_decimal(4, 333) == "0.(012)
