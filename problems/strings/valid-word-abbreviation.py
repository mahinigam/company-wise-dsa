"""Valid Word Abbreviation

Difficulty: Easy
Topic: strings
Preparation tags (not verified question attribution): Google, Amazon, Adobe
Source: https://leetcode.com/problems/valid-word-abbreviation/

Problem summary: Check whether an abbreviation matches a word; numeric runs skip characters and may not begin with zero.
Approach: Walk word and abbreviation indices, parsing each number into a skip length.
Complexity: O(n+m) time and O(1) space.
"""

def valid_word_abbreviation(word: str, abbr: str) -> bool:
    i = j = 0
    while i < len(word) and j < len(abbr):
        if abbr[j].isdigit():
            if abbr[j] == "0": return False
            skip = 0
            while j < len(abbr) and abbr[j].isdigit():
                skip = skip * 10 + int(abbr[j]); j += 1
            i += skip
        else:
            if word[i] != abbr[j]: return False
            i += 1; j += 1
    return i == len(word) and j == len(abbr)

assert valid_word_abbreviation("internationalization", "i12iz4n")
assert not valid_word_abbreviation("apple", "a2e")
assert not valid_word_abbreviation("apple", "a01e")
