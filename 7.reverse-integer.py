#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        u_limit = (2 ** 31) - 1
        l_limit = -(2 ** 31)

        # sanity check
        if x == 0 or x > u_limit or x < l_limit:
            return 0

        reversed_abs_str = str(abs(x))[::-1]

        if x > 0:
            if int(reversed_abs_str) < u_limit:
                return int(reversed_abs_str)
            else:
                return 0
        if x < 0:
            if -int(reversed_abs_str) > l_limit:

                return -int(reversed_abs_str)
            else:
                return 0

        #     reversed_neg_int = -reversed_int
        #     if reversed_neg_int > l_limit:
        #         return reversed_neg_int
        #     else:
        #         return 0


# @lc code=end

