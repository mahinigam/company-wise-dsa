"""Combination Sum

Difficulty: Medium
Topic: backtracking
Preparation tags (not verified question attribution): Amazon, Microsoft, Adobe
Source: https://leetcode.com/problems/combination-sum/

Problem summary: Find unique combinations of candidates that sum to target; each candidate may be reused.
Approach: Backtrack from a starting index and allow reuse of the selected candidate.
Complexity: Exponential output-sensitive time; O(target/min_candidate) recursion space.
"""

def combination_sum(candidates: list[int], target: int) -> list[list[int]]:
    candidates = sorted(set(candidates)); out = []
    def search(start, remaining, path):
        if remaining == 0: out.append(path[:]); return
        for i in range(start, len(candidates)):
            value = candidates[i]
            if value > remaining: break
            path.append(value); search(i, remaining - value, path); path.pop()
    search(0, target, [])
    return out

assert {tuple(x) for x in combination_sum([2,3,6,7], 7)} == {(2,2,3),(7,)}
assert combination_sum([2], 1) == []
assert combination_sum([2,3,5], 8)
