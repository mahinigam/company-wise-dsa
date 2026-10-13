"""Middle of the Linked List

Difficulty: Easy
Topic: linked-list
Preparation tags (not verified question attribution): Amazon, Microsoft, Adobe
Source: https://leetcode.com/problems/middle-of-the-linked-list/

Problem summary: Return the middle node; for even length, return the second middle.
Approach: Advance slow by one and fast by two steps.
Complexity: O(n) time, O(1) space.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val, self.next = val, next

def middle_node(head: ListNode | None) -> ListNode | None:
    slow = fast = head
    while fast and fast.next:
        slow, fast = slow.next, fast.next.next
    return slow

head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
assert middle_node(head).val == 3
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
assert middle_node(head).val == 3
