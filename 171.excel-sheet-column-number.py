#
# @lc app=leetcode id=171 lang=python3
#
# [171] Excel Sheet Column Number
#

# @lc code=start
class Solution:
    def titleToNumber(self, s: str) -> int:
        alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        current_sum = 0

        for c in s:
            current_sum = current_sum * 26 + alpha.find(c) + 1

        return current_sum


# @lc code=end

