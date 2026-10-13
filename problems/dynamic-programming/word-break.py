"""Word Break

Difficulty: Medium
Topic: dynamic-programming
Preparation tags (not verified question attribution): Google, Amazon, Microsoft
Source: https://leetcode.com/problems/word-break/

Problem summary: Check whether a string can be segmented into words from a dictionary.
Approach: DP marks each prefix as reachable if it can extend a previously reachable prefix by a dictionary word.
Complexity: O(n²) time in the straightforward version, O(n) space.
"""

def word_break(s: str, word_dict: list[str]) -> bool:
    words = set(word_dict); reachable = [False] * (len(s) + 1); reachable[0] = True
    max_len = max(map(len, words), default=0)
    for end in range(1, len(s) + 1):
        start_min = max(0, end - max_len)
        reachable[end] = any(reachable[start] and s[start:end] in words for start in range(start_min, end))
    return reachable[-1]

assert word_break("leetcode", ["leet", "code"])
assert word_break("applepenapple", ["apple", "pen"])
assert not word_break("catsandog", ["cats", "dog", "sand", "and", "cat"])
