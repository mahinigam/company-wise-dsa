"""Network Delay Time

Difficulty: Medium
Topic: graphs
Preparation tags (not verified question attribution): Amazon, Google, Uber
Source: https://leetcode.com/problems/network-delay-time/

Problem summary: Find how long it takes a signal from source k to reach every node in a positive-weight directed graph.
Approach: Run Dijkstra's algorithm with a min-heap and stale-entry checks.
Complexity: O((V+E) log V) time and O(V+E) space.
"""

import heapq

def network_delay_time(times: list[list[int]], n: int, k: int) -> int:
    graph = [[] for _ in range(n + 1)]
    for u, v, w in times: graph[u].append((v, w))
    dist = [float("inf")] * (n + 1); dist[k] = 0
    heap = [(0, k)]
    while heap:
        cost, node = heapq.heappop(heap)
        if cost != dist[node]: continue
        for nxt, weight in graph[node]:
            candidate = cost + weight
            if candidate < dist[nxt]:
                dist[nxt] = candidate; heapq.heappush(heap, (candidate, nxt))
    answer = max(dist[1:])
    return -1 if answer == float("inf") else int(answer)

assert network_delay_time([[2,1,1],[2,3,1],[3,4,1]], 4, 2) == 2
assert network_delay_time([[1,2,1]], 2, 2) == -1
