"""Max Points on a Line

Difficulty: Hard
Topic: geometry
Preparation tags (not verified question attribution): Google, Amazon, Meta
Source: https://leetcode.com/problems/max-points-on-a-line/

Problem summary: Find the maximum number of points lying on the same straight line.
Approach: For each anchor point, count normalized slopes to every other point using gcd.
Complexity: O(n²) time and O(n) space.
"""

from collections import defaultdict
from math import gcd

def max_points(points: list[list[int]]) -> int:
    if len(points) <= 2: return len(points)
    best = 1
    for i, (x1, y1) in enumerate(points):
        slopes = defaultdict(int); duplicates = 0; local = 0
        for x2, y2 in points[i + 1:]:
            dx, dy = x2 - x1, y2 - y1
            if dx == 0 and dy == 0:
                duplicates += 1; continue
            divisor = gcd(dx, dy); dx //= divisor; dy //= divisor
            if dx < 0: dx, dy = -dx, -dy
            elif dx == 0: dy = 1
            slopes[(dx, dy)] += 1
            local = max(local, slopes[(dx, dy)])
        best = max(best, local + duplicates + 1)
    return best

assert max_points([[1,1],[2,2],[3,3]]) == 3
assert max_points([[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]) == 4
assert max_points([[0,0],[0,0]]) == 2
