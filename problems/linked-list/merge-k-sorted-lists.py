"""Merge K Sorted Lists

Difficulty: Hard
Topic: linked-list
Preparation tags (not verified question attribution): Google, Amazon, Meta, Uber
Source: https://leetcode.com/problems/merge-k-sorted-lists/

Problem summary: Merge k sorted linked lists into one sorted linked list.
Approach: Keep the smallest available head from every list in a min-heap.
Complexity: O(N log k) time and O(k) heap space.
"""

import heapq
from itertools import count

class ListNode:
    def __init__(self, val=0, next=None):
        self.val, self.next = val, next

def merge_k_lists(lists: list[ListNode | None]) -> ListNode | None:
    heap = []; tie = count()
    for node in lists:
        if node: heapq.heappush(heap, (node.val, next(tie), node))
    dummy = tail = ListNode()
    while heap:
        _, _, node = heapq.heappop(heap)
        tail.next = node; tail = node
        if node.next: heapq.heappush(heap, (node.next.val, next(tie), node.next))
    tail.next = None
    return dummy.next

def chain(values):
    d = t = ListNode()
    for value in values: t.next = ListNode(value); t = t.next
    return d.next
def values(node):
    out = []
    while node: out.append(node.val); node = node.next
    return out

assert values(merge_k_lists([chain([1,4,5]), chain([1,3,4]), chain([2,6])])) == [1,1,2,3,4,4,5,6]
assert merge_k_lists([]) is None
