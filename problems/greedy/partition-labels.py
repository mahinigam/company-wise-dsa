"""Partition Labels

Difficulty: Medium
Topic: greedy
Preparation tags (not verified question attribution): Amazon, Meta, Google
Source: https://leetcode.com/problems/partition-labels/

Problem summary: Partition a string into as many parts as possible so each character appears in at most one part.
Approach: Record each character's last index and close a partition when the scan reaches the farthest last occurrence seen.
Complexity: O(n) time and O(k) space.
"""

def partition_labels(s: str) -> list[int]:
    last = {ch: i for i, ch in enumerate(s)}
    start = end = 0; sizes = []
    for i, ch in enumerate(s):
        end = max(end, last[ch])
        if i == end:
            sizes.append(end - start + 1); start = i + 1
    return sizes

assert partition_labels("ababcbacadefegdehijhklij") == [9,7,8]
assert partition_labels("eccbbbbdec") == [10]
assert partition_labels("") == []
