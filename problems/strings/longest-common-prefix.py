"""Longest Common Prefix

Difficulty: Easy
Topic: strings
Preparation tags (not verified question attribution): Accenture, Target, Adobe
Source: https://leetcode.com/problems/longest-common-prefix/

Problem summary: Find the longest prefix shared by every string.
Approach: Shrink the first word until every string starts with the candidate prefix.
Complexity: O(total characters compared) time, O(1) auxiliary space.
"""

def longest_common_prefix(strs: list[str]) -> str:
    if not strs: return ""
    prefix = strs[0]
    for word in strs[1:]:
        while not word.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix: return ""
    return prefix

assert longest_common_prefix(["flower", "flow", "flight"]) == "fl"
assert longest_common_prefix(["dog", "racecar", "car"]) == ""
assert longest_common_prefix([]) == ""
