"""Car Fleet

Difficulty: Medium
Topic: greedy
Preparation tags (not verified question attribution): Google, Amazon, Uber
Source: https://leetcode.com/problems/car-fleet/

Problem summary: Count groups of cars reaching the target together without passing each other.
Approach: Process cars from closest to the target backward and count increasing arrival times.
Complexity: O(n log n) time and O(n) space.
"""

def car_fleet(target: int, position: list[int], speed: list[int]) -> int:
    cars = sorted(zip(position, speed), reverse=True)
    fleets = 0; slowest_time = 0.0
    for pos, velocity in cars:
        arrival = (target - pos) / velocity
        if arrival > slowest_time:
            fleets += 1; slowest_time = arrival
    return fleets

assert car_fleet(12, [10,8,0,5,3], [2,4,1,1,3]) == 3
assert car_fleet(10, [3], [3]) == 1
assert car_fleet(100, [0,2,4], [4,2,1]) == 1
