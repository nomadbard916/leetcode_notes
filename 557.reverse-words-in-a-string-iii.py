#
# @lc app=leetcode id=557 lang=python3
#
# [557] Reverse Words in a String III
#

# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:
        word_list = s.split()

        reversed_list = [word[::-1] for word in word_list]

        return " ".join(reversed_list)


# @lc code=end

