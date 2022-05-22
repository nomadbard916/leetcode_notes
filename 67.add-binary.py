#
# @lc app=leetcode id=67 lang=python3
#
# [67] Add Binary
#

# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i, j, current_sum, ans = len(a) - 1, len(b) - 1, 0, ""
        while i >= 0 or j >= 0:
            if i >= 0:
                current_sum += int(a[i])
            if j >= 0:
                current_sum += int(b[j])

            remainder = current_sum % 2
            carry = current_sum // 2

            # the current_sum here is actually carried over to next iteration
            i, j, current_sum, ans = i - 1, j - 1, carry, str(remainder) + ans

        # consider remaining carry
        if current_sum != 0:
            ans = str(current_sum) + ans

        return ans

        # sol2
        # return bin(int(a, 2) + int(b, 2))[2:]


# @lc code=end
