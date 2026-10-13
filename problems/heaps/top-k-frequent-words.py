"""Top K Frequent Words

Difficulty: Medium
Topic: heaps
Preparation tags (not verified question attribution): Amazon, Google, Meta
Source: https://leetcode.com/problems/top-k-frequent-words/

Problem summary: Return the k most frequent words, breaking ties lexicographically.
Approach: Count words and sort by descending frequency then ascending spelling.
Complexity: O(n log n) time and O(n) space.
"""

from collections import Counter

def top_k_frequent_words(words: list[str], k: int) -> list[str]:
    counts = Counter(words)
    return sorted(counts, key=lambda word: (-counts[word], word))[:k]

assert top_k_frequent_words(["i","love","leetcode","i","love","coding"], 2) == ["i", "love"]
assert top_k_frequent_words(["the","day","is"," sunny","the","the","the","sunny","is","is"], 4) == ["the", "is", "sunny", "day"]
