"""Number of Provinces

Difficulty: Medium
Topic: graphs
Preparation tags (not verified question attribution): Amazon, Microsoft, Meta
Source: https://leetcode.com/problems/number-of-provinces/

Problem summary: Count connected groups in an adjacency matrix representing an undirected graph.
Approach: DFS each unvisited city and mark every city reachable from it.
Complexity: O(n²) time and O(n) extra space.
"""

def find_circle_num(is_connected: list[list[int]]) -> int:
    n = len(is_connected); seen = set(); provinces = 0
    for city in range(n):
        if city in seen: continue
        provinces += 1; stack = [city]; seen.add(city)
        while stack:
            node = stack.pop()
            for nxt, connected in enumerate(is_connected[node]):
                if connected and nxt not in seen:
                    seen.add(nxt); stack.append(nxt)
    return provinces

assert find_circle_num([[1,1,0],[1,1,0],[0,0,1]]) == 2
assert find_circle_num([[1,0,0],[0,1,0],[0,0,1]]) == 3
