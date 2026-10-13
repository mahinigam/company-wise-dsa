"""Min Cost Climbing Stairs

Difficulty: Easy
Topic: dynamic-programming
Preparation tags (not verified question attribution): Amazon, Microsoft, Adobe
Source: https://leetcode.com/problems/min-cost-climbing-stairs/

Problem summary: Find the minimum cost to reach beyond the final stair when each move climbs one or two steps.
Approach: Maintain the minimal costs for the two previous positions.
Complexity: O(n) time and O(1) space.
"""

def min_cost_climbing_stairs(cost: list[int]) -> int:
    two_back = one_back = 0
    for value in cost:
        two_back, one_back = one_back, value + min(two_back, one_back)
    return min(two_back, one_back)

assert min_cost_climbing_stairs([10,15,20]) == 15
assert min_cost_climbing_stairs([1,100,1,1,1,100,1,1,100,1]) == 6
assert min_cost_climbing_stairs([]) == 0
