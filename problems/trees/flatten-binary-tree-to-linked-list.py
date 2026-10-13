"""Flatten Binary Tree to Linked List

Difficulty: Medium
Topic: trees
Preparation tags (not verified question attribution): Amazon, Microsoft, Meta
Source: https://leetcode.com/problems/flatten-binary-tree-to-linked-list/

Problem summary: Flatten a binary tree in place into a right-only preorder chain.
Approach: Use a stack to remember right subtrees and splice each node's left child onto the right.
Complexity: O(n) time and O(h) stack space.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right

def flatten(root: TreeNode | None) -> None:
    if root is None: return
    stack = [root]
    previous = None
    while stack:
        node = stack.pop()
        if node.right: stack.append(node.right)
        if node.left: stack.append(node.left)
        if previous:
            previous.left = None
            previous.right = node
        previous = node

root = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(5, None, TreeNode(6)))
flatten(root)
values = []
while root:
    assert root.left is None
    values.append(root.val); root = root.right
assert values == [1,2,3,4,5,6]
