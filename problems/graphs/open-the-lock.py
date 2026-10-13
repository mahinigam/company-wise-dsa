"""Open the Lock

Difficulty: Medium
Topic: graphs
Preparation tags (not verified question attribution): Google, Amazon, Uber
Source: https://leetcode.com/problems/open-the-lock/

Problem summary: Find the minimum wheel turns to reach target without visiting dead-end combinations.
Approach: BFS over the 10,000 possible four-digit states.
Complexity: O(10^4) time and space bound.
"""

from collections import deque

def open_lock(deadends: list[str], target: str) -> int:
    blocked = set(deadends)
    if "0000" in blocked: return -1
    queue, seen = deque([("0000", 0)]), {"0000"}
    while queue:
        state, steps = queue.popleft()
        if state == target: return steps
        for i, ch in enumerate(state):
            digit = int(ch)
            for delta in (-1, 1):
                nxt_digit = (digit + delta) % 10
                nxt = state[:i] + str(nxt_digit) + state[i+1:]
                if nxt not in seen and nxt not in blocked:
                    seen.add(nxt); queue.append((nxt, steps + 1))
    return -1

assert open_lock(["0201","0101","0102","1212","2002"], "0202") == 6
assert open_lock(["8888"], "0009") == 1
assert open_lock(["0000"], "8888") == -1
