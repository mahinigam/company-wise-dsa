"""Evaluate Reverse Polish Notation

Difficulty: Medium
Topic: stack-queue
Preparation tags (not verified question attribution): Uber, Amazon, Microsoft
Source: https://leetcode.com/problems/evaluate-reverse-polish-notation/

Problem summary: Evaluate an arithmetic expression written in postfix notation.
Approach: Use a stack; pop right and left operands whenever an operator appears.
Complexity: O(n) time and O(n) space.
"""

def eval_rpn(tokens: list[str]) -> int:
    stack = []
    for token in tokens:
        if token in {"+", "-", "*", "/"}:
            right, left = stack.pop(), stack.pop()
            if token == "+": value = left + right
            elif token == "-": value = left - right
            elif token == "*": value = left * right
            else: value = int(left / right)
            stack.append(value)
        else:
            stack.append(int(token))
    return stack[-1]

assert eval_rpn(["2", "1", "+", "3", "*"]) == 9
assert eval_rpn(["4", "13", "5", "/", "+"]) == 6
assert eval_rpn(["-7", "3", "/"]) == -2
