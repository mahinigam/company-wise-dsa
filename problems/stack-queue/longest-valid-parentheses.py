"""Longest Valid Parentheses

Difficulty: Hard
Topic: stack-queue
Preparation tags (not verified question attribution): Google, Amazon, Meta
Source: https://leetcode.com/problems/longest-valid-parentheses/

Problem summary: Find the longest contiguous valid parentheses substring.
Approach: Store unmatched opening indices and use the last invalid position as a boundary.
Complexity: O(n) time and O(n) space.
"""

def longest_valid_parentheses(s: str) -> int:
    stack = [-1]; best = 0
    for i, ch in enumerate(s):
        if ch == "(": stack.append(i)
        else:
            stack.pop()
            if not stack: stack.append(i)
            else: best = max(best, i - stack[-1])
    return best

assert longest_valid_parentheses("(()") == 2
assert longest_valid_parentheses(")()())") == 4
assert longest_valid_parentheses("") == 0
