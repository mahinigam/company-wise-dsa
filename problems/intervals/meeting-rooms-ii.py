"""Meeting Rooms II

Difficulty: Medium
Topic: intervals
Preparation tags (not verified question attribution): Google, Amazon, Uber
Source: https://www.geeksforgeeks.org/dsa/minimum-number-platforms-required-railwaybus-station/

Problem summary: Compute the minimum number of rooms needed to schedule all meetings.
Approach: Sort starts and use a min-heap of active meeting end times.
Complexity: O(n log n) time and O(n) space.
"""

import heapq

def min_meeting_rooms(intervals: list[list[int]]) -> int:
    active = []
    for start, end in sorted(intervals):
        if active and active[0] <= start: heapq.heappop(active)
        heapq.heappush(active, end)
    return len(active)

assert min_meeting_rooms([[0,30],[5,10],[15,20]]) == 2
assert min_meeting_rooms([[7,10],[2,4]]) == 1
assert min_meeting_rooms([]) == 0
