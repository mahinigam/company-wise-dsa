"""Sort List

Difficulty: Medium
Topic: linked-list
Preparation tags (not verified question attribution): Google, Amazon, Microsoft
Source: https://leetcode.com/problems/sort-list/

Problem summary: Sort a linked list in O(n log n) time.
Approach: Use merge sort: split around the middle, sort both halves, and merge.
Complexity: O(n log n) time and O(log n) recursion space.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val, self.next = val, next

def sort_list(head: ListNode | None) -> ListNode | None:
    if head is None or head.next is None: return head
    slow, fast = head, head.next
    while fast and fast.next: slow, fast = slow.next, fast.next.next
    second, slow.next = slow.next, None
    a, b = sort_list(head), sort_list(second)
    dummy = tail = ListNode()
    while a and b:
        if a.val <= b.val: tail.next, a = a, a.next
        else: tail.next, b = b, b.next
        tail = tail.next
    tail.next = a or b
    return dummy.next

def chain(vals):
    d = t = ListNode()
    for v in vals: t.next = ListNode(v); t = t.next
    return d.next
def values(node):
    out = []
    while node: out.append(node.val); node = node.next
    return out

assert values(sort_list(chain([4,2,1,3]))) == [1,2,3,4]
assert values(sort_list(chain([-1,5,3,4,0]))) == [-1,0,3,4,5]
assert sort_list(None) is None
