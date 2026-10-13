"""Serialize and Deserialize Binary Tree

Difficulty: Hard
Topic: trees
Preparation tags (not verified question attribution): Google, Amazon, Meta
Source: https://leetcode.com/problems/serialize-and-deserialize-binary-tree/

Problem summary: Convert a binary tree to a string and reconstruct the same structure.
Approach: Preorder DFS records explicit null markers so child boundaries are preserved.
Complexity: O(n) time and O(n) space.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right

class Codec:
    def serialize(self, root):
        out = []
        def visit(node):
            if node is None: out.append("#"); return
            out.append(str(node.val)); visit(node.left); visit(node.right)
        visit(root)
        return ",".join(out)
    def deserialize(self, data):
        values = iter(data.split(","))
        def build():
            value = next(values)
            if value == "#": return None
            node = TreeNode(int(value)); node.left = build(); node.right = build()
            return node
        return build()

codec = Codec()
tree = TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4), TreeNode(5)))
encoded = codec.serialize(tree); restored = codec.deserialize(encoded)
assert codec.serialize(restored) == encoded
assert codec.serialize(None) == "#"
