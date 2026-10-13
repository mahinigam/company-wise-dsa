"""N-Queens

Difficulty: Hard
Topic: backtracking
Preparation tags (not verified question attribution): Google, Amazon, Meta
Source: https://leetcode.com/problems/n-queens/

Problem summary: Place n queens on an n×n board so no two queens attack each other.
Approach: Backtrack row by row while tracking occupied columns and diagonals.
Complexity: Exponential search time; O(n) auxiliary space excluding boards.
"""

def solve_n_queens(n: int) -> list[list[str]]:
    out = []; columns = set(); diag1 = set(); diag2 = set(); placement = []
    def search(row):
        if row == n:
            board = []
            for col in placement:
                board.append("." * col + "Q" + "." * (n - col - 1))
            out.append(board); return
        for col in range(n):
            if col in columns or row - col in diag1 or row + col in diag2: continue
            columns.add(col); diag1.add(row-col); diag2.add(row+col); placement.append(col)
            search(row + 1)
            placement.pop(); columns.remove(col); diag1.remove(row-col); diag2.remove(row+col)
    search(0)
    return out

assert len(solve_n_queens(4)) == 2
assert solve_n_queens(1) == [["Q"]]
assert solve_n_queens(2) == []
