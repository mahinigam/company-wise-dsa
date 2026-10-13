"""2 Keys Keyboard

Difficulty: Medium
Topic: dynamic-programming
Preparation tags (not verified question attribution): Google, Amazon, Adobe
Source: https://leetcode.com/problems/2-keys-keyboard/

Problem summary: Find the minimum copy-all and paste operations needed to create n 'A' characters.
Approach: The optimal operation count is the sum of prime factors of n.
Complexity: O(sqrt n) time and O(1) space.
"""

def min_steps(n: int) -> int:
    answer, factor = 0, 2
    while factor * factor <= n:
        while n % factor == 0:
            answer += factor; n //= factor
        factor += 1
    if n > 1: answer += n
    return answer

assert min_steps(1) == 0
assert min_steps(3) == 3
assert min_steps(9) == 6
