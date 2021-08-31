#
# @lc app=leetcode id=504 lang=python3
#
# [504] Base 7
#

# @lc code=start
class Solution:
    def convertToBase7(self, num: int) -> str:
        # sanity check first
        if num == 0:
            return "0"

        sign = "" if num >= 0 else "-"

        abs_num = abs(num)

        result = ""

        while abs_num > 0:
            remainder = abs_num % 7

            result = str(remainder) + result

            abs_num = abs_num // 7

        return sign + str(result)


# @lc code=end

