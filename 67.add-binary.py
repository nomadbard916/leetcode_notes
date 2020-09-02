#
# @lc app=leetcode id=67 lang=python3
#
# [67] Add Binary
#

# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ans = ""
        i, j, current_sum = len(a) - 1, len(b) - 1, 0
        while i >= 0 or j >= 0 or current_sum == 1:
            current_sum += int(a[i]) if i >= 0 else 0
            current_sum += int(b[j]) if j >= 0 else 0
            ans = str(current_sum % 2) + ans
            i, j, current_sum = i - 1, j - 1, current_sum // 2
        return ans

        # sol2
        # return bin(int(a, 2) + int(b, 2))[2:]


# @lc code=end

