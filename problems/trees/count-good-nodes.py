"""Count Good Nodes in Binary Tree

Difficulty: Medium
Topic: trees
Preparation tags (not verified question attribution): Amazon, Google, Uber
Source: https://leetcode.com/problems/count-good-nodes-in-binary-tree/

Problem summary: Count nodes whose value is at least every value on the root-to-node path.
Approach: DFS carries the maximum ancestor value and counts qualifying nodes.
Complexity: O(n) time and O(h) recursion space.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right

def good_nodes(root: TreeNode | None) -> int:
    def visit(node, largest):
        if node is None: return 0
        good = int(node.val >= largest)
        largest = max(largest, node.val)
        return good + visit(node.left, largest) + visit(node.right, largest)
    return visit(root, float("-inf"))

assert good_nodes(TreeNode(3, TreeNode(1, TreeNode(3)), TreeNode(4, TreeNode(1), TreeNode(5)))) == 4
assert good_nodes(None) == 0
