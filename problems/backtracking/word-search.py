"""Word Search

Difficulty: Medium
Topic: backtracking
Preparation tags (not verified question attribution): Amazon, Microsoft, Meta
Source: https://leetcode.com/problems/word-search/

Problem summary: Determine whether a word can be traced through adjacent horizontal/vertical cells without reusing a cell.
Approach: DFS from each matching first character and temporarily mark cells in the active path.
Complexity: O(rows×cols·4^L) worst case, O(L) recursion space.
"""

def exist(board: list[list[str]], word: str) -> bool:
    if not word: return True
    if not board or not board[0]: return False
    rows, cols = len(board), len(board[0])
    def dfs(r, c, i):
        if i == len(word): return True
        if not (0 <= r < rows and 0 <= c < cols) or board[r][c] != word[i]: return False
        ch = board[r][c]; board[r][c] = "\0"
        found = dfs(r+1,c,i+1) or dfs(r-1,c,i+1) or dfs(r,c+1,i+1) or dfs(r,c-1,i+1)
        board[r][c] = ch
        return found
    return any(dfs(r,c,0) for r in range(rows) for c in range(cols))

board = [list("ABCE"), list("SFCS"), list("ADEE")]
assert exist(board, "ABCCED")
assert exist(board, "SEE")
assert not exist(board, "ABCB")
