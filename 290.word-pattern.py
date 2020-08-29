#
# @lc app=leetcode id=290 lang=python3
#
# [290] Word Pattern
#

# @lc code=start
class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        char_word: dict = {}
        word_char: dict = {}

        words = str.split()

        # sanity check
        if len(words) != len(pattern):
            return False

        for c, w in zip(pattern, words):
            if c not in char_word:
                # duplicated mapping happens
                if w in word_char:
                    return False
                else:
                    char_word[c] = w
                    char_word[w] = c
            else:
                if char_word[c] != w:
                    return False

        return True


# @lc code=end

