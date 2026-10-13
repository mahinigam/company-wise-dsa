"""Climbing Stairs

Difficulty: Easy
Topic: dynamic-programming
Preparation tags (not verified question attribution): Amazon, Adobe, Accenture
Source: https://leetcode.com/problems/climbing-stairs/

Problem summary: Count ways to reach step n when each move climbs one or two steps.
Approach: The count follows a Fibonacci recurrence.
Complexity: O(n) time and O(1) space.
"""

def climb_stairs(n: int) -> int:
    if n < 0: return 0
    a, b = 1, 1
    for _ in range(n): a, b = b, a + b
    return a

assert climb_stairs(2) == 2
assert climb_stairs(3) == 3
assert climb_stairs(0) == 1
