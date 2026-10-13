"""Copy List With Random Pointer

Difficulty: Medium
Topic: linked-list
Preparation tags (not verified question attribution): Amazon, Microsoft, Meta
Source: https://leetcode.com/problems/copy-list-with-random-pointer/

Problem summary: Deep-copy a linked list whose nodes also have arbitrary random pointers.
Approach: Map each original node identity to a copy and then wire next/random references.
Complexity: O(n) time and O(n) space.
"""

class Node:
    def __init__(self, x: int, next=None, random=None):
        self.val, self.next, self.random = x, next, random

def copy_random_list(head: Node | None) -> Node | None:
    if head is None: return None
    copies = {}
    node = head
    while node:
        copies[node] = Node(node.val); node = node.next
    node = head
    while node:
        copies[node].next = copies.get(node.next)
        copies[node].random = copies.get(node.random)
        node = node.next
    return copies[head]

a, b = Node(7), Node(13); a.next, b.next = b, None; a.random, b.random = None, a
c = copy_random_list(a)
assert c is not a and c.val == 7 and c.next.val == 13 and c.next.random is c
assert copy_random_list(None) is None
