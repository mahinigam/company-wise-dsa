"""Simplify Path

Difficulty: Medium
Topic: stack-queue
Preparation tags (not verified question attribution): Amazon, Microsoft, Uber
Source: https://leetcode.com/problems/simplify-path/

Problem summary: Canonicalize a Unix-style absolute path.
Approach: Split path components, ignore empty and '.', and pop for '..' when possible.
Complexity: O(n) time and O(n) space.
"""

def simplify_path(path: str) -> str:
    stack = []
    for part in path.split("/"):
        if part in ("", "."): continue
        if part == "..":
            if stack: stack.pop()
        else: stack.append(part)
    return "/" + "/".join(stack)

assert simplify_path("/home/") == "/home"
assert simplify_path("/../") == "/"
assert simplify_path("/home//foo/") == "/home/foo"
assert simplify_path("/a/./b/../../c/") == "/c"
