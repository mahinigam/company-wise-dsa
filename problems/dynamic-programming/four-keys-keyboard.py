"""4 Keys Keyboard

Difficulty: Hard
Topic: dynamic-programming
Preparation tags (not verified question attribution): Google, Amazon, Microsoft
Source: https://leetcode.com/problems/4-keys-keyboard/

Problem summary: Maximize printed A characters in n key presses using A, select-all, copy, and paste.
Approach: DP compares printing one more A with selecting/copying at an earlier point and pasting repeatedly.
Complexity: O(n²) time and O(n) space.
"""

def max_a(n: int) -> int:
    dp = list(range(n + 1))
    for presses in range(4, n + 1):
        for copy_at in range(1, presses - 2):
            dp[presses] = max(dp[presses], dp[copy_at] * (presses - copy_at - 1))
    return dp[n]

assert max_a(3) == 3
assert max_a(7) == 9
assert max_a(9) == 16
