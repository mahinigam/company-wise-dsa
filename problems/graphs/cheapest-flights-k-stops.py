"""Cheapest Flights Within K Stops

Difficulty: Medium
Topic: graphs
Preparation tags (not verified question attribution): Amazon, Google, Uber
Source: https://leetcode.com/problems/cheapest-flights-within-k-stops/

Problem summary: Find the cheapest price from source to destination using at most k stops.
Approach: Use bounded Bellman–Ford rounds; each round adds at most one flight to a route.
Complexity: O((k+1)E) time and O(V) space.
"""

def find_cheapest_price(n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
    inf = float("inf")
    prices = [inf] * n; prices[src] = 0
    for _ in range(k + 1):
        updated = prices.copy()
        for u, v, price in flights:
            if prices[u] != inf and prices[u] + price < updated[v]:
                updated[v] = prices[u] + price
        prices = updated
    return -1 if prices[dst] == inf else int(prices[dst])

assert find_cheapest_price(4, [[0,1,100],[1,2,100],[2,3,100],[0,3,500]], 0, 3, 1) == 500
assert find_cheapest_price(3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 1) == 200
