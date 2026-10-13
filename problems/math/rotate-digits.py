"""Rotate Digits

Difficulty: Easy
Topic: math
Preparation tags (not verified question attribution): Amazon, Target, Adobe
Source: https://leetcode.com/problems/rotated-digits/

Problem summary: Count positive integers from 1 to n that become a different valid number after rotating digits by 180 degrees.
Approach: Check each digit: 3,4,7 invalidate; 2,5,6,9 make the number change.
Complexity: O(n log n) time and O(1) extra space.
"""

def rotated_digits(n: int) -> int:
    invalid = set("347")
    changing = set("2569")
    answer = 0
    for value in range(1, n + 1):
        text = str(value)
        if any(ch in invalid for ch in text): continue
        if any(ch in changing for ch in text): answer += 1
    return answer

assert rotated_digits(10) == 4
assert rotated_digits(1) == 0
assert rotated_digits(20) == 9
