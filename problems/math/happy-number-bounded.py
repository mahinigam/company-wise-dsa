"""Happy Number: Cycle Detection

Difficulty: Easy
Topic: math
Preparation tags (not verified question attribution): Google, Amazon, Microsoft
Source: https://leetcode.com/problems/happy-number/

Problem summary: Detect whether repeated squared-digit sums reach 1 using constant auxiliary space.
Approach: Floyd's cycle detection is applied to the deterministic digit-sum transform.
Complexity: O(log n) transform work per step and O(1) space.
"""

def is_happy_floyd(n: int) -> bool:
    def advance(value):
        total = 0
        while value:
            value, digit = divmod(value, 10)
            total += digit * digit
        return total
    slow, fast = n, advance(n)
    while fast != 1 and slow != fast:
        slow = advance(slow)
        fast = advance(advance(fast))
    return fast == 1

assert is_happy_floyd(19)
assert not is_happy_floyd(2)
