"""Reverse Linked List II

Difficulty: Medium
Topic: linked-list
Preparation tags (not verified question attribution): Amazon, Microsoft, Meta
Source: https://leetcode.com/problems/reverse-linked-list-ii/

Problem summary: Reverse a linked-list segment from position left through right (1-indexed).
Approach: Move to the node before the segment and repeatedly move the next node to the segment front.
Complexity: O(n) time and O(1) space.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val, self.next = val, next

def reverse_between(head: ListNode | None, left: int, right: int) -> ListNode | None:
    dummy = ListNode(0, head); before = dummy
    for _ in range(left - 1): before = before.next
    current = before.next
    for _ in range(right - left):
        moving = current.next
        current.next = moving.next
        moving.next = before.next
        before.next = moving
    return dummy.next

def chain(vals):
    d = t = ListNode()
    for v in vals: t.next = ListNode(v); t = t.next
    return d.next
def values(node):
    out = []
    while node: out.append(node.val); node = node.next
    return out

assert values(reverse_between(chain([1,2,3,4,5]), 2, 4)) == [1,4,3,2,5]
assert values(reverse_between(chain([5]), 1, 1)) == [5]
