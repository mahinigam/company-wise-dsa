"""Linked List Cycle

Difficulty: Easy
Topic: linked-list
Preparation tags (not verified question attribution): Amazon, Microsoft, Adobe
Source: https://leetcode.com/problems/linked-list-cycle/

Problem summary: Detect whether a linked list contains a cycle.
Approach: Use Floyd's slow and fast pointers; they meet if a cycle exists.
Complexity: O(n) time, O(1) space.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val, self.next = val, next

def has_cycle(head: ListNode | None) -> bool:
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast: return True
    return False

a, b, c = ListNode(1), ListNode(2), ListNode(3)
a.next, b.next, c.next = b, c, b
assert has_cycle(a)
assert not has_cycle(ListNode(1, ListNode(2)))
