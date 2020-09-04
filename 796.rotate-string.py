#
# @lc app=leetcode id=796 lang=python3
#
# [796] Rotate String
#

# @lc code=start
class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        if not A and not B:
            return True

        if not A or not B:
            return False

        if len(A) > len(B):
            return False

        return A in B + B


# @lc code=end

