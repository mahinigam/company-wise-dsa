"""Valid Parenthesis String

Difficulty: Medium
Topic: greedy
Preparation tags (not verified question attribution): Google, Amazon, Meta
Source: https://leetcode.com/problems/valid-parenthesis-string/

Problem summary: Check whether parentheses are valid when '*' can represent '(', ')', or empty.
Approach: Track the minimum and maximum possible unmatched opening counts while scanning.
Complexity: O(n) time and O(1) space.
"""

def check_valid_string(s: str) -> bool:
    low = high = 0
    for ch in s:
        if ch == "(": low += 1; high += 1
        elif ch == ")": low -= 1; high -= 1
        else: low -= 1; high += 1
        if high < 0: return False
        low = max(low, 0)
    return low == 0

assert check_valid_string("(*)")
assert check_valid_string("(*))")
assert not check_valid_string("(((*)")
