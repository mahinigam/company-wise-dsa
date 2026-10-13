"""Rotate List

Difficulty: Medium
Topic: linked-list
Preparation tags (not verified question attribution): Amazon, Microsoft, Meta
Source: https://leetcode.com/problems/rotate-list/

Problem summary: Rotate a linked list to the right by k places.
Approach: Compute the length, connect tail to head, then break the ring at the new tail.
Complexity: O(n) time and O(1) space.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val, self.next = val, next

def rotate_right(head: ListNode | None, k: int) -> ListNode | None:
    if head is None or head.next is None or k == 0: return head
    length, tail = 1, head
    while tail.next: tail = tail.next; length += 1
    k %= length
    if k == 0: return head
    tail.next = head
    steps = length - k
    new_tail = tail
    for _ in range(steps): new_tail = new_tail.next
    new_head = new_tail.next; new_tail.next = None
    return new_head

def chain(vals):
    d = t = ListNode()
    for v in vals: t.next = ListNode(v); t = t.next
    return d.next
def values(node):
    out = []
    while node: out.append(node.val); node = node.next
    return out

assert values(rotate_right(chain([1,2,3,4,5]), 2)) == [4,5,1,2,3]
assert values(rotate_right(chain([0,1,2]), 4)) == [2,0,1]
