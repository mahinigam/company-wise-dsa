"""Add Two Numbers

Difficulty: Medium
Topic: linked-list
Preparation tags (not verified question attribution): Amazon, Microsoft, Meta
Source: https://leetcode.com/problems/add-two-numbers/

Problem summary: Add two non-negative integers represented in reverse digit order by linked lists.
Approach: Walk both lists together while carrying overflow to the next digit.
Complexity: O(max(n,m)) time and O(1) auxiliary space excluding output.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val, self.next = val, next

def add_two_numbers(l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
    dummy = tail = ListNode()
    carry = 0
    while l1 or l2 or carry:
        a = l1.val if l1 else 0
        b = l2.val if l2 else 0
        carry, digit = divmod(a + b + carry, 10)
        tail.next = ListNode(digit); tail = tail.next
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
    return dummy.next

def chain(vals):
    d = t = ListNode()
    for x in vals: t.next = ListNode(x); t = t.next
    return d.next
def values(node):
    out = []
    while node: out.append(node.val); node = node.next
    return out

assert values(add_two_numbers(chain([2, 4, 3]), chain([5, 6, 4]))) == [7, 0, 8]
assert values(add_two_numbers(chain([0]), chain([0]))) == [0]
