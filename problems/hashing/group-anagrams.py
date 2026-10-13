"""Group Anagrams

Difficulty: Medium
Topic: hashing
Preparation tags (not verified question attribution): Amazon, Meta, Adobe, Uber
Source: https://leetcode.com/problems/group-anagrams/

Problem summary: Group strings that are anagrams of one another.
Approach: Use each word's sorted characters as a canonical dictionary key.
Complexity: O(n · k log k) time for n words of maximum length k.
"""

from collections import defaultdict


def group_anagrams(strs: list[str]) -> list[list[str]]:
    groups: dict[str, list[str]] = defaultdict(list)
    for word in strs:
        groups["".join(sorted(word))].append(word)
    return list(groups.values())


assert {frozenset(g) for g in group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])} == {
    frozenset({"eat", "tea", "ate"}), frozenset({"tan", "nat"}), frozenset({"bat"})
}
assert group_anagrams([]) == []
