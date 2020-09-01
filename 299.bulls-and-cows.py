from collections import defaultdict

#
# @lc app=leetcode id=299 lang=python3
#
# [299] Bulls and Cows
#

# @lc code=start
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0
        cows = 0

        secret_counted = defaultdict(int)

        for s, g in zip(secret, guess):
            if g == s:
                bulls += 1
            else:
                secret_counted[s] += 1

        for s, g in zip(secret, guess):
            if g != s and secret_counted[g] != 0:
                cows += 1
                secret_counted[g] -= 1

        return f"{bulls}A{cows}B"


# @lc code=end

