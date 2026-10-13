"""Reorder List

Difficulty: Medium
Topic: linked-list
Preparation tags (not verified question attribution): Amazon, Meta, Uber
Source: https://leetcode.com/problems/reorder-list/

Problem summary: Reorder L0→L1→…→Ln into L0→Ln→L1→Ln-1→… in place.
Approach: Find the middle, reverse the second half, then interleave both halves.
Complexity: O(n) time, O(1) space.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val, self.next = val, next

def reorder_list(head: ListNode | None) -> None:
    if not head or not head.next: return
    slow = fast = head
    while fast.next and fast.next.next:
        slow, fast = slow.next, fast.next.next
    second = slow.next; slow.next = None
    previous = None
    while second:
        second.next, previous, second = previous, second, second.next
    first, second = head, previous
    while second:
        first_next, second_next = first.next, second.next
        first.next, second.next = second, first_next
        first, second = first_next, second_next

def chain(vals):
    d = t = ListNode()
    for x in vals: t.next = ListNode(x); t = t.next
    return d.next
def values(node):
    out = []
    while node: out.append(node.val); node = node.next
    return out

head = chain([1, 2, 3, 4]); reorder_list(head); assert values(head) == [1, 4, 2, 3]
head = chain([1, 2, 3, 4, 5]); reorder_list(head); assert values(head) == [1, 5, 2, 4, 3]
