"""Remove Nth Node From End

Difficulty: Medium
Topic: linked-list
Preparation tags (not verified question attribution): Amazon, Microsoft, Meta
Source: https://leetcode.com/problems/remove-nth-node-from-end-of-list/

Problem summary: Remove the nth node from the end of a list.
Approach: Advance a fast pointer n steps, then move fast and slow together from a sentinel.
Complexity: O(n) time, O(1) space.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val, self.next = val, next

def remove_nth_from_end(head: ListNode | None, n: int) -> ListNode | None:
    dummy = ListNode(0, head)
    fast = slow = dummy
    for _ in range(n):
        if fast.next is None: raise ValueError("n exceeds list length")
        fast = fast.next
    while fast.next:
        fast, slow = fast.next, slow.next
    slow.next = slow.next.next
    return dummy.next

def chain(vals):
    d = t = ListNode()
    for x in vals: t.next = ListNode(x); t = t.next
    return d.next
def values(node):
    out = []
    while node: out.append(node.val); node = node.next
    return out

assert values(remove_nth_from_end(chain([1, 2, 3, 4, 5]), 2)) == [1, 2, 3, 5]
assert values(remove_nth_from_end(chain([1]), 1)) == []
