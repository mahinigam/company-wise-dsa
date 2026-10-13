"""Generate Parentheses

Difficulty: Medium
Topic: backtracking
Preparation tags (not verified question attribution): Amazon, Microsoft, Google
Source: https://leetcode.com/problems/generate-parentheses/

Problem summary: Generate all combinations of n pairs of well-formed parentheses.
Approach: Backtrack while never using more closing than opening brackets.
Complexity: O(Cn) output-sensitive time for Catalan number Cn; O(n) recursion space.
"""

def generate_parenthesis(n: int) -> list[str]:
    out = []
    def build(current, opened, closed):
        if len(current) == 2 * n:
            out.append(current); return
        if opened < n: build(current + "(", opened + 1, closed)
        if closed < opened: build(current + ")", opened, closed + 1)
    build("", 0, 0)
    return out

assert set(generate_parenthesis(3)) == {"((()))","(()())","(())()","()(())","()()()"}
assert generate_parenthesis(1) == ["()"]
assert generate_parenthesis(0) == [""]
