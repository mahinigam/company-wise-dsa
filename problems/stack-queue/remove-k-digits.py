"""Remove K Digits

Difficulty: Medium
Topic: stack-queue
Preparation tags (not verified question attribution): Google, Amazon, Uber
Source: https://leetcode.com/problems/remove-k-digits/

Problem summary: Remove k digits from a number string to make the smallest possible number.
Approach: Use a monotonic increasing stack, removing larger previous digits when a smaller digit arrives.
Complexity: O(n) time and O(n) space.
"""

def remove_kdigits(num: str, k: int) -> str:
    stack = []
    for digit in num:
        while k and stack and stack[-1] > digit:
            stack.pop(); k -= 1
        stack.append(digit)
    if k: stack = stack[:-k]
    result = "".join(stack).lstrip("0")
    return result or "0"

assert remove_kdigits("1432219", 3) == "1219"
assert remove_kdigits("10200", 1) == "200"
assert remove_kdigits("10", 2) == "0"
