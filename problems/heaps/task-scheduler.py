"""Task Scheduler

Difficulty: Medium
Topic: heaps
Preparation tags (not verified question attribution): Google, Amazon, Meta
Source: https://leetcode.com/problems/task-scheduler/

Problem summary: Find the minimum number of intervals to execute tasks with n cooldown intervals between equal tasks.
Approach: The most frequent task determines the minimum frame size; compare it with the task count.
Complexity: O(n) time and O(1) extra space for a fixed alphabet.
"""

from collections import Counter

def least_interval(tasks: list[str], n: int) -> int:
    if not tasks: return 0
    counts = Counter(tasks)
    maximum = max(counts.values())
    tied = sum(count == maximum for count in counts.values())
    frame = (maximum - 1) * (n + 1) + tied
    return max(len(tasks), frame)

assert least_interval(["A","A","A","B","B","B"], 2) == 8
assert least_interval(["A","A","A","B","B","B"], 0) == 6
assert least_interval([], 2) == 0
