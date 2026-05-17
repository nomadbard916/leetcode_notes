#
# @lc app=leetcode id=91 lang=python3
# @lcpr version=30403
#
# [91] Decode Ways
#

# @lc code=start


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
        n = len(s)
        dp = [0] * n

        for i, digit_char in enumerate(s):
            if i == 0:
                if digit_char == 0:
                    dp[i] = 0
                else:
                    dp[i] = 1
                continue
            if i == 1:
                if digit_char == 0:
                    dp[i] = dp[i - 1]
                else:
                    dp[i] = dp[i] + dp[i - 1]
                continue

            if digit_char == "0":
                dp[i] = dp[i - 1]
                continue

            # consider only 1 digit
            if s[i - 1] != "0":
                dp[i] += dp[i - 1]
            # consider two digits
            two_digits = int(s[i - 2 : i])
            if 10 <= two_digits <= 26:
                dp[i] += dp[i - 2]

        return dp[-1]


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
