"""Meeting Rooms

Difficulty: Easy
Topic: intervals
Preparation tags (not verified question attribution): Google, Microsoft, Amazon
Source: https://www.geeksforgeeks.org/dsa/find-minimum-number-of-meeting-rooms-required-for-a-given-number-of-meetings/

Problem summary: Determine whether a person can attend every meeting interval.
Approach: Sort by start and ensure each meeting starts no earlier than the previous meeting ends.
Complexity: O(n log n) time and O(1) auxiliary space.
"""

def can_attend_meetings(intervals: list[list[int]]) -> bool:
    intervals = sorted(intervals)
    return all(intervals[i][0] >= intervals[i - 1][1] for i in range(1, len(intervals)))

assert can_attend_meetings([[0,30],[5,10],[15,20]]) is False
assert can_attend_meetings([[7,10],[2,4]]) is True
assert can_attend_meetings([]) is True
