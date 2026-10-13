"""Remove Duplicates From Sorted List II

Difficulty: Medium
Topic: linked-list
Preparation tags (not verified question attribution): Amazon, Microsoft, Adobe
Source: https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/

Problem summary: Remove every value that appears more than once in a sorted linked list.
Approach: Use a sentinel and skip duplicate runs entirely.
Complexity: O(n) time and O(1) space.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val, self.next = val, next

def delete_duplicates(head: ListNode | None) -> ListNode | None:
    dummy = ListNode(0, head); previous = dummy
    while head:
        if head.next and head.val == head.next.val:
            duplicate = head.val
            while head and head.val == duplicate: head = head.next
            previous.next = head
        else:
            previous, head = head, head.next
    return dummy.next

def chain(vals):
    d = t = ListNode()
    for v in vals: t.next = ListNode(v); t = t.next
    return d.next
def values(node):
    out = []
    while node: out.append(node.val); node = node.next
    return out

assert values(delete_duplicates(chain([1,2,3,3,4,4,5]))) == [1,2,5]
assert values(delete_duplicates(chain([1,1,1,2,3]))) == [2,3]
assert delete_duplicates(chain([1,1])) is None
