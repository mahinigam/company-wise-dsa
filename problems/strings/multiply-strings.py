"""Multiply Strings

Difficulty: Medium
Topic: strings
Preparation tags (not verified question attribution): Google, Amazon, Meta
Source: https://leetcode.com/problems/multiply-strings/

Problem summary: Multiply two non-negative integers represented as decimal strings without converting them to integers.
Approach: Use grade-school digit multiplication and accumulate carries into a result array.
Complexity: O(nm) time and O(n+m) space.
"""

def multiply(num1: str, num2: str) -> str:
    if num1 == "0" or num2 == "0": return "0"
    m, n = len(num1), len(num2)
    result = [0] * (m + n)
    for i in range(m - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            product = int(num1[i]) * int(num2[j]) + result[i + j + 1]
            result[i + j + 1] = product % 10
            result[i + j] += product // 10
    return "".join(map(str, result)).lstrip("0") or "0"

assert multiply("2", "3") == "6"
assert multiply("123", "456") == "56088"
assert multiply("0", "52") == "0"
