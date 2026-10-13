"""Word Break II

Difficulty: Hard
Topic: dynamic-programming
Preparation tags (not verified question attribution): Google, Amazon, Meta
Source: https://leetcode.com/problems/word-break-ii/

Problem summary: Return all sentences formed by segmenting a string into dictionary words.
Approach: Memoize sentence suffixes for each start index to avoid recomputing the same suffix.
Complexity: Output-sensitive exponential time; O(n) recursion plus memoized results.
"""

from functools import lru_cache

def word_break_sentences(s: str, word_dict: list[str]) -> list[str]:
    words = set(word_dict)
    @lru_cache(None)
    def build(start):
        if start == len(s): return ("",)
        out = []
        for end in range(start + 1, len(s) + 1):
            word = s[start:end]
            if word in words:
                for suffix in build(end):
                    out.append(word if not suffix else word + " " + suffix)
        return tuple(out)
    return list(build(0))

assert set(word_break_sentences("catsanddog", ["cat","cats","and","sand","dog"])) == {"cats and dog", "cat sand dog"}
assert word_break_sentences("catsandog", ["cats","dog","sand","and","cat"]) == []
