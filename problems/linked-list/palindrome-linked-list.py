"""Palindrome Linked List

Difficulty: Easy
Topic: linked-list
Preparation tags (not verified question attribution): Amazon, Microsoft, Meta
Source: https://leetcode.com/problems/palindrome-linked-list/

Problem summary: Determine if linked-list values read the same forward and backward.
Approach: Copy values and compare with their reverse; this simple version prioritizes clarity.
Complexity: O(n) time, O(n) space.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val, self.next = val, next

def is_palindrome_list(head: ListNode | None) -> bool:
    values = []
    while head:
        values.append(head.val)
        head = head.next
    return values == values[::-1]

assert is_palindrome_list(ListNode(1, ListNode(2, ListNode(2, ListNode(1)))))
assert not is_palindrome_list(ListNode(1, ListNode(2)))
