"""Basic Calculator II

Difficulty: Medium
Topic: stack-queue
Preparation tags (not verified question attribution): Google, Amazon, Microsoft
Source: https://leetcode.com/problems/basic-calculator-ii/

Problem summary: Evaluate a string containing non-negative integers and +, -, *, / with standard precedence.
Approach: Accumulate each signed term on a stack; multiply/divide the last term immediately.
Complexity: O(n) time and O(n) space.
"""

def calculate(s: str) -> int:
    stack = []; number = 0; previous = "+"
    for i, ch in enumerate(s + "+"):
        if ch.isdigit(): number = number * 10 + int(ch)
        elif ch == " ": continue
        else:
            if previous == "+": stack.append(number)
            elif previous == "-": stack.append(-number)
            elif previous == "*": stack.append(stack.pop() * number)
            elif previous == "/":
                last = stack.pop()
                stack.append(int(last / number))
            previous = ch; number = 0
    return sum(stack)

assert calculate("3+2*2") == 7
assert calculate(" 3/2 ") == 1
assert calculate(" 3+5 / 2 ") == 5
