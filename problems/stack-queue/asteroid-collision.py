"""Asteroid Collision

Difficulty: Medium
Topic: stack-queue
Preparation tags (not verified question attribution): Amazon, Google, Uber
Source: https://leetcode.com/problems/asteroid-collision/

Problem summary: Simulate collisions between asteroids moving in opposite directions.
Approach: Only a positive asteroid followed by a negative asteroid can collide; resolve using a stack.
Complexity: O(n) time and O(n) space.
"""

def asteroid_collision(asteroids: list[int]) -> list[int]:
    stack = []
    for asteroid in asteroids:
        alive = True
        while alive and asteroid < 0 and stack and stack[-1] > 0:
            if stack[-1] < -asteroid: stack.pop()
            elif stack[-1] == -asteroid:
                stack.pop(); alive = False
            else:
                alive = False
        if alive: stack.append(asteroid)
    return stack

assert asteroid_collision([5, 10, -5]) == [5, 10]
assert asteroid_collision([8, -8]) == []
assert asteroid_collision([10, 2, -5]) == [10]
