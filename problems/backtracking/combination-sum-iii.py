"""Combination Sum III

Difficulty: Medium
Topic: backtracking
Preparation tags (not verified question attribution): Amazon, Microsoft, Adobe
Source: https://leetcode.com/problems/combination-sum-iii/

Problem summary: Choose k distinct digits from 1..9 that sum to n.
Approach: Backtrack through increasing digits and prune when the remaining sum is impossible.
Complexity: Exponential search bounded by 9 choices; O(k) recursion space.
"""

def combination_sum3(k: int, n: int) -> list[list[int]]:
    out = []
    def search(start, remaining, path):
        if len(path) == k:
            if remaining == 0: out.append(path[:])
            return
        for value in range(start, 10):
            if value > remaining: break
            path.append(value); search(value + 1, remaining - value, path); path.pop()
    search(1, n, [])
    return out

assert combination_sum3(3, 7) == [[1,2,4]]
assert combination_sum3(3, 9) == [[1,2,6],[1,3,5],[2,3,4]]
assert combination_sum3(4, 1) == []
