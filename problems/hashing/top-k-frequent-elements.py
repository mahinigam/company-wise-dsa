"""Top K Frequent Elements

Difficulty: Medium
Topic: hashing
Preparation tags (not verified question attribution): Amazon, Google, Meta, Uber
Source: https://leetcode.com/problems/top-k-frequent-elements/

Problem summary: Return the k values with the highest frequency.
Approach: Count values and sort distinct entries by descending frequency.
Complexity: O(n log n) time and O(n) space.
"""

from collections import Counter


def top_k_frequent(nums: list[int], k: int) -> list[int]:
    counts = Counter(nums)
    return [value for value, _ in sorted(counts.items(), key=lambda item: (-item[1], item[0]))[:k]]


assert top_k_frequent([1, 1, 1, 2, 2, 3], 2) == [1, 2]
assert top_k_frequent([4, 4, 5], 1) == [4]
