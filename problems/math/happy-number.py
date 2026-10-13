"""Happy Number

Difficulty: Easy
Topic: math
Preparation tags (not verified question attribution): Google, Amazon, Microsoft
Source: https://leetcode.com/problems/happy-number/

Problem summary: Determine whether repeated sum of squared digits reaches 1.
Approach: Apply the digit transform until reaching 1 or repeating a state.
Complexity: O(log n) per transform; O(cycle length) space.
"""

def is_happy(n: int) -> bool:
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        total = 0
        while n:
            n, digit = divmod(n, 10)
            total += digit * digit
        n = total
    return n == 1

assert is_happy(19)
assert not is_happy(2)
