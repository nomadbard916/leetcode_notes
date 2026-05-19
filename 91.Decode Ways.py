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
        letter mapping
        - different ways
        - grouping
        - partition
        - count
        - map
        * pattern kws
        - backtracking?
        - two pointer? ...no
        - recursion?
        - dp?

        * constraint kws
        answer in 32-bit integer
        * map to algo
        * mental model
        - consider one-digit or two-digits
        - identical to climbing stairs
        * tricky
        - each code cannot start from 0
        - code range can only be 1~26
        * problem specific pattern
        dp[i] = number of ways to decode s[:i]
        - 1-char step: if s[i-1] != '0' → dp[i] += dp[i-1]
        - 2-char step: if 10 ≤ int(s[i-2:i]) ≤ 26 → dp[i] += dp[i-2]
        """

        # * Key Insights
        # 1. This is Climbing Stairs in disguise.
        # At each character, you decide: "do I consume 1 digit or 2?"
        # If valid, both branches contribute. This produces the same recurrence as Fibonacci.
        # 2. The dp table visualized for "226":
        # i | s[:i] | dp[i] | reasoning
        # 0 | "" | 1 | base case: empty = 1 way
        # 1 | "2" | 1 | "B"
        # 2 | "22" | 2 | "BB" or "V"
        # 3 | "226" | 3 | "BBF", "VF", "BZ"
        # 3. Zero is a trap character — it has two failure modes:
        # s[i] == '0' → 1-digit step is dead
        # s[i-2:i] starts with '0' (e.g. "06") → 2-digit step is dead (checked by 10 ≤ x ≤ 26)
        # 4. Space optimization is clean here — since each dp[i] only looks back 2 positions,
        # you can replace the array with two rolling variables (prev1, prev2), reducing space from O(n) to O(1).

        #! sol1: DP table
        n = len(s)

        # dp[i] = number of ways to decode s[:i]
        # n+1: sentinel
        dp = [0] * (n + 1)
        # dp[0] = 1  → empty prefix: one way to decode nothing (base case),
        # though it won't happen in test cases
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
