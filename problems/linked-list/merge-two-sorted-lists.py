"""Merge Two Sorted Lists

Difficulty: Easy
Topic: linked-list
Preparation tags (not verified question attribution): Microsoft, Amazon, Meta
Source: https://leetcode.com/problems/merge-two-sorted-lists/

Problem summary: Merge two sorted linked lists into one sorted list.
Approach: Use a sentinel node and repeatedly attach the smaller current node.
Complexity: O(n+m) time, O(1) auxiliary space.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val, self.next = val, next

def merge_two_lists(list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
    sentinel = tail = ListNode()
    while list1 and list2:
        if list1.val <= list2.val:
            tail.next, list1 = list1, list1.next
        else:
            tail.next, list2 = list2, list2.next
        tail = tail.next
    tail.next = list1 or list2
    return sentinel.next

def chain(values):
    dummy = tail = ListNode()
    for value in values: tail.next = ListNode(value); tail = tail.next
    return dummy.next
def values(head):
    out = []
    while head: out.append(head.val); head = head.next
    return out

assert values(merge_two_lists(chain([1, 2, 4]), chain([1, 3, 4]))) == [1, 1, 2, 3, 4, 4]
assert merge_two_lists(None, None) is None
