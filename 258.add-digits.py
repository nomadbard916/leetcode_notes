#
# @lc app=leetcode id=258 lang=python3
#
# [258] Add Digits
#

# @lc code=start
class Solution:
    def addDigits(self, num: int) -> int:
        num_s = str(num)

        while len(num_s) > 1:
            current_sum = 0
            for digit_s in num_s:
                current_sum += int(digit_s)

            num_s = str(current_sum)

        return int(num_s)


# @lc code=end

