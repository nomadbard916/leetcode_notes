#
# @lc app=leetcode id=171 lang=python3
#
# [171] Excel Sheet Column Number
#

# @lc code=start
class Solution:
    def titleToNumber(self, s: str) -> int:
        #  eg. 1234 = 1* (10**3) + 2 * (10**2) + 3 * (10**1) +4 *(10**0)
        alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        current_sum = 0
        current_digit = len(s)

        for c in s:
            current_sum += (alpha.find(c) + 1) * (26 ** (current_digit - 1))
            current_digit -= 1

        return current_sum


# @lc code=end

