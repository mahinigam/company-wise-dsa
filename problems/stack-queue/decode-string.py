"""Decode String

Difficulty: Medium
Topic: stack-queue
Preparation tags (not verified question attribution): Google, Amazon, Meta
Source: https://leetcode.com/problems/decode-string/

Problem summary: Decode nested patterns such as 3[a2[c]].
Approach: Use a stack to preserve the prior string and repetition count at each opening bracket.
Complexity: O(output length) time and O(n) auxiliary space.
"""

def decode_string(s: str) -> str:
    stack = []; current = ""; number = 0
    for ch in s:
        if ch.isdigit(): number = number * 10 + int(ch)
        elif ch == "[":
            stack.append((current, number)); current, number = "", 0
        elif ch == "]":
            prefix, repeats = stack.pop(); current = prefix + current * repeats
        else: current += ch
    return current

assert decode_string("3[a]2[bc]") == "aaabcbc"
assert decode_string("3[a2[c]]") == "accaccacc"
assert decode_string("2[abc]3[cd]ef") == "abcabccdcdcdef
