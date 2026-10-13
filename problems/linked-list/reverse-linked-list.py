"""Reverse Linked List

Difficulty: Easy
Topic: linked-list
Preparation tags (not verified question attribution): Microsoft, Amazon, Adobe, Accenture
Source: https://leetcode.com/problems/reverse-linked-list/

Problem summary: Reverse a singly linked list.
Approach: Iteratively redirect each next pointer toward the previous node.
Complexity: O(n) time, O(1) space.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val, self.next = val, next

def reverse_list(head: ListNode | None) -> ListNode | None:
    previous = None
    while head:
        following = head.next
        head.next = previous
        previous, head = head, following
    return previous

def to_list(head):
    out = []
    while head: out.append(head.val); head = head.next
    return out

head = ListNode(1, ListNode(2, ListNode(3)))
assert to_list(reverse_list(head)) == [3, 2, 1]
assert reverse_list(None) is None
