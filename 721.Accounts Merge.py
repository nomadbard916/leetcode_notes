#
# @lc app=leetcode id=721 lang=python3
# @lcpr version=30201
#
# [721] Accounts Merge
#

# @lc code=start
from collections import defaultdict
from typing import Dict, List


class UnionFind:
    def __init__(self, n) -> None:
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            # Path compression
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)

        if px == py:
            return

        # union by rank
        if self.rank[px] < self.rank[py]:
            px, py = py, px

        self.parent[py] = px

        if self.rank[px] == self.rank[py]:
            self.rank[px] += 1


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # Key points:
        # - A person can have any number of accounts initially, but all of their accounts definitely have the same name GitHubLeetCode
        # - After merging the accounts, return the accounts in the following format: the first element of each account is the name, and the rest of the elements are emails in sorted order GitHubLeetCode
        # - Even accounts with the same name may belong to different people if they don't share emails
        # ! sol1: union find, which is the common solution
        n = len(accounts)
        uf = UnionFind(n)

        # Map email to the first account index that contains it
        email_to_account: Dict[str, int] = {}

        # Build the union-find structure
        for i, account in enumerate(accounts):
            # Skip the name (first element)
            for email in account[1:]:
                if email in email_to_account:
                    # Union this account with the account that first had this email
                    uf.union(i, email_to_account[email])
                else:
                    # First time seeing this email
                    email_to_account[email] = i

        # Group accounts by their root parent
        groups = defaultdict(list)
        for i in range(n):
            root = uf.find(i)
            groups[root].append(i)

        # Build the result
        result = []
        for account_indices in groups.values():
            emails = set()
            name = ""
            for idx in account_indices:
                if not name:
                    name = accounts[idx][0]
                emails.update(accounts[idx][1:])

            # Create the merged account: [name] + sorted emails
            merged_account = [name] + sorted(emails)
            result.append(merged_account)

        return result

        # ! sol2: graph DFS


# @lc code=end


#
# @lcpr case=start
# \n[["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]\n
# @lcpr case=end

# @lcpr case=start
# \n[["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe1@m.co"],["Kevin","Kevin3@m.co","Kevin5@m.co","Kevin0@m.co"],["Ethan","Ethan5@m.co","Ethan4@m.co","Ethan0@m.co"],["Hanzo","Hanzo3@m.co","Hanzo1@m.co","Hanzo0@m.co"],["Fern","Fern5@m.co","Fern1@m.co","Fern0@m.co"]]\n
# @lcpr case=end

#
