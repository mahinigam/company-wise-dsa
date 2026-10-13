"""Word Ladder

Difficulty: Hard
Topic: graphs
Preparation tags (not verified question attribution): Google, Amazon, Meta
Source: https://leetcode.com/problems/word-ladder/

Problem summary: Find the shortest transformation length between two words, changing one letter at a time through dictionary words.
Approach: BFS explores transformation layers; wildcard buckets identify words one letter apart.
Complexity: O(N·L²) time for N words of length L; O(N·L) space.
"""

from collections import defaultdict, deque

def ladder_length(begin_word: str, end_word: str, word_list: list[str]) -> int:
    words = set(word_list)
    if end_word not in words: return 0
    buckets = defaultdict(list)
    for word in words | {begin_word}:
        for i in range(len(word)):
            buckets[word[:i] + "*" + word[i+1:]].append(word)
    queue, seen = deque([(begin_word, 1)]), {begin_word}
    while queue:
        word, length = queue.popleft()
        if word == end_word: return length
        for i in range(len(word)):
            key = word[:i] + "*" + word[i+1:]
            for nxt in buckets[key]:
                if nxt not in seen:
                    seen.add(nxt); queue.append((nxt, length + 1))
            buckets[key].clear()
    return 0

assert ladder_length("hit", "cog", ["hot","dot","dog","lot","log","cog"]) == 5
assert ladder_length("hit", "cog", ["hot","dot","dog","lot","log"]) == 0
