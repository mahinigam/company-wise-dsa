"""Plus One

Difficulty: Easy
Topic: math
Preparation tags (not verified question attribution): Accenture, Target, Adobe
Source: https://leetcode.com/problems/plus-one/

Problem summary: Increment a non-negative integer represented as digits.
Approach: Walk from the least significant digit, carrying through nines as needed.
Complexity: O(n) time and O(n) output space.
"""

def plus_one(digits: list[int]) -> list[int]:
    for i in range(len(digits) - 1, -1, -1):
        if digits[i] < 9:
            digits[i] += 1
            return digits
        digits[i] = 0
    return [1] + digits

assert plus_one([1,2,3]) == [1,2,4]
assert plus_one([4,3,2,1]) == [4,3,2,2]
assert plus_one([9,9,9]) == [1,0,0,0]
