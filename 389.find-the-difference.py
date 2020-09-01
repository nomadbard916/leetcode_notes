from collections import Counter

#
# @lc app=leetcode id=389 lang=python3
#
# [389] Find the Difference
#

# @lc code=start
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:

        diff_count = Counter(t) - Counter(s)

        for char, count in diff_count.items():
            if count == 1:
                return char


# @lc code=end

