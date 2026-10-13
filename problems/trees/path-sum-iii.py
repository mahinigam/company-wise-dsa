"""Path Sum III

Difficulty: Medium
Topic: trees
Preparation tags (not verified question attribution): Amazon, Google, Meta
Source: https://leetcode.com/problems/path-sum-iii/

Problem summary: Count downward paths that sum to target; a path may start and end anywhere.
Approach: Use prefix-sum frequencies during DFS to count paths ending at the current node.
Complexity: O(n) average time and O(h) active-prefix space.
"""

from collections import defaultdict

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right

def path_sum_count(root: TreeNode | None, target_sum: int) -> int:
    prefix = defaultdict(int, {0: 1})
    def visit(node, total):
        if node is None: return 0
        total += node.val
        count = prefix[total - target_sum]
        prefix[total] += 1
        count += visit(node.left, total) + visit(node.right, total)
        prefix[total] -= 1
        return count
    return visit(root, 0)

root = TreeNode(10, TreeNode(5, TreeNode(3, TreeNode(3), TreeNode(-2)), TreeNode(2, None, TreeNode(1))), TreeNode(-3, None, TreeNode(11)))
assert path_sum_count(root, 8) == 3
assert path_sum_count(None, 0) == 0
