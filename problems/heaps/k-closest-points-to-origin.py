"""K Closest Points to Origin

Difficulty: Medium
Topic: heaps
Preparation tags (not verified question attribution): Amazon, Google, Uber
Source: https://leetcode.com/problems/k-closest-points-to-origin/

Problem summary: Return k points with the smallest squared Euclidean distance to the origin.
Approach: Select points ordered by squared distance; square roots are unnecessary.
Complexity: O(n log n) time and O(n) space in this baseline.
"""

def k_closest(points: list[list[int]], k: int) -> list[list[int]]:
    if not 0 <= k <= len(points): raise ValueError("k out of range")
    return sorted(points, key=lambda p: p[0] * p[0] + p[1] * p[1])[:k]

assert {tuple(p) for p in k_closest([[1,3],[-2,2],[2,-2]], 2)} == {(-2,2),(2,-2)}
assert k_closest([[3,3],[5,-1],[-2,4]], 1) == [[3,3]]
