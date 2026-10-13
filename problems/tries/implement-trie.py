"""Implement Trie (Prefix Tree)

Difficulty: Medium
Topic: tries
Preparation tags (not verified question attribution): Google, Amazon, Microsoft
Source: https://leetcode.com/problems/implement-trie-prefix-tree/

Problem summary: Support insertion, exact word search, and prefix search.
Approach: Each node maps characters to child nodes and stores whether a word ends there.
Complexity: O(L) per operation for word length L; O(total stored characters) space.
"""

class TrieNode:
    def __init__(self):
        self.children = {}
        self.terminal = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            node = node.children.setdefault(ch, TrieNode())
        node.terminal = True
    def _walk(self, text: str):
        node = self.root
        for ch in text:
            if ch not in node.children: return None
            node = node.children[ch]
        return node
    def search(self, word: str) -> bool:
        node = self._walk(word)
        return node is not None and node.terminal
    def starts_with(self, prefix: str) -> bool:
        return self._walk(prefix) is not None

trie = Trie(); trie.insert("apple")
assert trie.search("apple") and not trie.search("app")
assert trie.starts_with("app")
trie.insert("app"); assert trie.search("app")
