"""Maximum Width of Binary Tree

Difficulty: Medium
Topic: trees
Preparation tags (not verified question attribution): Google, Amazon, Meta
Source: https://leetcode.com/problems/maximum-width-of-binary-tree/

Problem summary: Find the maximum width of a tree level, counting gaps between end nodes.
Approach: BFS assigns complete-tree positional indices and normalizes them at each level.
Complexity: O(n) time and O(w) queue space.
"""

from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right

def width_of_binary_tree(root: TreeNode | None) -> int:
    if root is None: return 0
    queue = deque([(root, 0)]); best = 0
    while queue:
        level_size = len(queue); base = queue[0][1]; first = last = 0
        for i in range(level_size):
            node, index = queue.popleft(); index -= base
            if i == 0: first = index
            if i == level_size - 1: last = index
            if node.left: queue.append((node.left, 2 * index))
            if node.right: queue.append((node.right, 2 * index + 1))
        best = max(best, last - first + 1)
    return best

root = TreeNode(1, TreeNode(3, TreeNode(5), TreeNode(3)), TreeNode(2, None, TreeNode(9)))
assert width_of_binary_tree(root) == 4
assert width_of_binary_tree(None) == 0
