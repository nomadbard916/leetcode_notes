#
# @lc app=leetcode id=520 lang=python3
#
# [520] Detect Capital
#

# @lc code=start
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word.lower() == word:
            return True

        if word.upper() == word:
            return True

        for i, char in enumerate(word):
            if i == 0 and char.isupper():
                continue

            if char.isupper():
                return False

        return True


# @lc code=end

