"""Group Shifted Strings

Difficulty: Medium
Topic: strings
Preparation tags (not verified question attribution): Google, Adobe, Target
Source: https://leetcode.com/problems/group-shifted-strings/

Problem summary: Group strings that differ only by a uniform cyclic shift of each character.
Approach: Normalize each string by offsets from its first character modulo 26.
Complexity: O(total characters) expected time and space.
"""

from collections import defaultdict

def group_shifted_strings(strings: list[str]) -> list[list[str]]:
    groups = defaultdict(list)
    for word in strings:
        if not word: key = ()
        else:
            base = ord(word[0]) - ord("a")
            key = tuple((ord(ch) - ord("a") - base) % 26 for ch in word)
        groups[key].append(word)
    return [sorted(group) for _, group in sorted(groups.items(), key=lambda item: str(item[0]))]

result = group_shifted_strings(["abc","bcd","acef","xyz","az","ba","a","z"])
assert any(set(g) == {"abc","bcd","xyz"} for g in result)
assert any(set(g) == {"az","ba"} for g in result)
