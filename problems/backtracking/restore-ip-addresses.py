"""Restore IP Addresses

Difficulty: Medium
Topic: backtracking
Preparation tags (not verified question attribution): Amazon, Microsoft, Meta
Source: https://leetcode.com/problems/restore-ip-addresses/

Problem summary: Insert three dots into a digit string to form valid IPv4 addresses.
Approach: Backtrack over segment lengths 1..3, rejecting leading zeroes and values above 255.
Complexity: O(1) bounded search for input length under typical constraints.
"""

def restore_ip_addresses(s: str) -> list[str]:
    out = []
    def search(index, parts):
        remaining_parts = 4 - len(parts)
        remaining_chars = len(s) - index
        if remaining_chars < remaining_parts or remaining_chars > 3 * remaining_parts: return
        if len(parts) == 4:
            if index == len(s): out.append(".".join(parts))
            return
        for width in range(1, 4):
            piece = s[index:index + width]
            if len(piece) != width or (width > 1 and piece[0] == "0"): continue
            if int(piece) <= 255: search(index + width, parts + [piece])
    search(0, [])
    return out

assert set(restore_ip_addresses("25525511135")) == {"255.255.11.135", "255.255.111.35"}
assert restore_ip_addresses("0000") == ["0.0.0.0"]
assert restore_ip_addresses("1111") == ["1.1.1.1"]
