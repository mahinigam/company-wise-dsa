"""Min Cost to Connect All Points

Difficulty: Medium
Topic: graphs
Preparation tags (not verified question attribution): Google, Amazon, Uber
Source: https://leetcode.com/problems/min-cost-to-connect-all-points/

Problem summary: Connect all 2D points with minimum total Manhattan distance.
Approach: Prim's minimum-spanning-tree algorithm adds the cheapest edge crossing from visited to unvisited points.
Complexity: O(n²) time and O(n) space.
"""

def min_cost_connect_points(points: list[list[int]]) -> int:
    n = len(points)
    if n <= 1: return 0
    used = [False] * n; distance = [float("inf")] * n; distance[0] = 0
    total = 0
    for _ in range(n):
        node = min((i for i in range(n) if not used[i]), key=lambda i: distance[i])
        used[node] = True; total += distance[node]
        x, y = points[node]
        for j, (a, b) in enumerate(points):
            if not used[j]: distance[j] = min(distance[j], abs(x-a) + abs(y-b))
    return int(total)

assert min_cost_connect_points([[0,0],[2,2],[3,10],[5,2],[7,0]]) == 20
assert min_cost_connect_points([[3,12],[-2,5],[-4,1]]) == 18
assert min_cost_connect_points([[1,1]]) == 0
