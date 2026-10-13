"""Min Stack

Difficulty: Medium
Topic: stack-queue
Preparation tags (not verified question attribution): Amazon, Microsoft, Meta
Source: https://leetcode.com/problems/min-stack/

Problem summary: Implement a stack that returns its minimum in O(1).
Approach: Store each value with the minimum observed at that stack depth.
Complexity: O(1) per operation; O(n) space.
"""

class MinStack:
    def __init__(self):
        self._items: list[tuple[int, int]] = []
    def push(self, val: int) -> None:
        current_min = min(val, self._items[-1][1]) if self._items else val
        self._items.append((val, current_min))
    def pop(self) -> None:
        self._items.pop()
    def top(self) -> int:
        return self._items[-1][0]
    def get_min(self) -> int:
        return self._items[-1][1]

st = MinStack(); st.push(-2); st.push(0); st.push(-3)
assert st.get_min() == -3
st.pop(); assert st.top() == 0 and st.get_min() == -2
