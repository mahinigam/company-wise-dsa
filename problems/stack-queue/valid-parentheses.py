"""Valid Parentheses

Difficulty: Easy
Topic: stack-queue
Preparation tags (not verified question attribution): Amazon, Microsoft, Adobe, Accenture
Source: https://leetcode.com/problems/valid-parentheses/

Problem summary: Determine whether bracket pairs are correctly nested.
Approach: Push opening brackets and match each closing bracket against the stack top.
Complexity: O(n) time and O(n) space.
"""

def is_valid(s: str) -> bool:
    stack = []
    pairs = {")": "(", "]": "[", "}": "{"}
    for ch in s:
        if ch in pairs:
            if not stack or stack.pop() != pairs[ch]: return False
        else:
            stack.append(ch)
    return not stack

assert is_valid("()[]{}")
assert not is_valid("(]")
assert not is_valid("(")
assert is_valid("")
