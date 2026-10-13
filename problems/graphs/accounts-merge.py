"""Accounts Merge

Difficulty: Medium
Topic: graphs
Preparation tags (not verified question attribution): Google, Amazon, Meta
Source: https://leetcode.com/problems/accounts-merge/

Problem summary: Merge accounts sharing at least one email; output each merged email set sorted.
Approach: Union accounts that share an email and group emails by their final representative.
Complexity: O(N log N) time due to sorting; O(N) space.
"""

def accounts_merge(accounts: list[list[str]]) -> list[list[str]]:
    parent = list(range(len(accounts)))
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]; x = parent[x]
        return x
    owner = {}
    for i, account in enumerate(accounts):
        for email in account[1:]:
            if email in owner: parent[find(i)] = find(owner[email])
            else: owner[email] = i
    groups = {}
    for email, i in owner.items(): groups.setdefault(find(i), set()).add(email)
    return [[accounts[i][0]] + sorted(emails) for i, emails in sorted(groups.items())]

out = accounts_merge([["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]])
assert len(out) == 3
assert out[0][0] == "John" and out[0][1:] == ["john00@mail.com","john_newyork@mail.com","johnsmith@mail.com"]
