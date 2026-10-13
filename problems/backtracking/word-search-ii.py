"""Word Search II

Difficulty: Hard
Topic: backtracking
Preparation tags (not verified question attribution): Google, Amazon, Meta
Source: https://leetcode.com/problems/word-search-ii/

Problem summary: Find all dictionary words present as non-repeating paths in a character grid.
Approach: Build a trie of target words and DFS once per board cell, pruning paths when no trie prefix matches.
Complexity: Input-dependent, often much faster than searching each word separately; O(total dictionary characters) trie space.
"""

def find_words(board: list[list[str]], words: list[str]) -> list[str]:
    if not board or not board[0] or not words: return []
    trie = {}
    for word in words:
        node = trie
        for ch in word: node = node.setdefault(ch, {})
        node["$"] = word
    rows, cols = len(board), len(board[0]); found = set()
    def dfs(r, c, node):
        ch = board[r][c]
        if ch not in node: return
        nxt = node[ch]
        if "$" in nxt: found.add(nxt.pop("$"))
        board[r][c] = "#"
        for nr,nc in ((r-1,c),(r+1,c),(r,c-1),(r,c+1)):
            if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] != "#":
                dfs(nr,nc,nxt)
        board[r][c] = ch
        if not nxt: node.pop(ch)
    for r in range(rows):
        for c in range(cols): dfs(r,c,trie)
    return sorted(found)

board = [list("oaan"), list("etae"), list("ihkr"), list("iflv")]
assert find_words(board, ["oath","pea","eat","rain"]) == ["eat","oath"]
assert find_words([list("ab"), list("cd")], ["abcd"]) == []
