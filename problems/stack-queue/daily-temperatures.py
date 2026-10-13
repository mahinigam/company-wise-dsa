"""Daily Temperatures

Difficulty: Medium
Topic: stack-queue
Preparation tags (not verified question attribution): Amazon, Meta, Google
Source: https://leetcode.com/problems/daily-temperatures/

Problem summary: For each day, find how many days until a warmer temperature.
Approach: Maintain a monotonic stack of unresolved indices.
Complexity: O(n) time and O(n) space.
"""

def daily_temperatures(temperatures: list[int]) -> list[int]:
    answer = [0] * len(temperatures)
    stack = []
    for i, temp in enumerate(temperatures):
        while stack and temperatures[stack[-1]] < temp:
            j = stack.pop()
            answer[j] = i - j
        stack.append(i)
    return answer

assert daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73]) == [1, 1, 4, 2, 1, 1, 0, 0]
assert daily_temperatures([30, 40, 50, 60]) == [1, 1, 1, 0]
