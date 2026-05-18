#
# @lc app=leetcode id=91 lang=python3
# @lcpr version=30403
#
# [91] Decode Ways
#

# @lc code=start
from __future__ import annotations


class Solution:
    def numDecodings(self, s: str) -> int:
        """
        * noun and verb
        - string of numbers
        - decoded
        - rules:
        prefix 0 not allowed
        1~26
        - different ways
        - grouping
        * pattern kws
        - backtracking?
        - two pointer? ...no
        - recursion?
        - dp?

        * constraint kws
        answer in 32-bit integer
        * map to algo
        * mental model
        * tricky
        - each code cannot start from 0
        - code range can only be 1~26
        * problem specific pattern
        """
        #! sol1: DP table
        n = len(s)

        # dp[i] = number of ways to decode s[:i]
        # n+1: sentinel
        dp = [0] * (n + 1)
        # dp[0] = 1  → empty prefix: one way to decode nothing (base case)
        dp[0] = 1
        dp[1] = 1 if s[0] != "0" else 0

        for i in range(2, n + 1):
            # ── 1-digit decode: just the current character ──
            one_digit = int(s[i - 1])
            if one_digit != 0:
                # s[i-1] alone is a valid letter (1–9)
                dp[i] += dp[i - 1]

            # ── 2-digit decode: current + previous character ──
            # e.g. s[1:3] → "26"
            two_digits = int(s[i - 2 : i])
            if 10 <= two_digits <= 26:
                # s[i-2:i] is a valid letter (10–26)
                dp[i] += dp[i - 2]

        return dp[-1]

        # Time:  O(n)
        # Space: O(n)


# @lc code=end


#
# @lcpr case=start
# "12"\n
# @lcpr case=end

# @lcpr case=start
# "226"\n
# @lcpr case=end

# @lcpr case=start
# "06"\n
# @lcpr case=end

#
