#
# @lc app=leetcode id=168 lang=python3
#
# [168] Excel Sheet Column Title
#

# @lc code=start
class Solution:
    def convertToTitle(self, n: int) -> str:
        alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        s = ""

        # sanity check
        if n < 1:
            return s

        while n > 0:
            n, alpha_order = divmod(n, 26)

            # must be z
            if alpha_order == 0:
                n -= 1
                current_alpha = alpha[-1]
            else:
                current_alpha = alpha[alpha_order - 1]

            s = current_alpha + s

        return s


# @lc code=end

