#
# @lc app=leetcode id=344 lang=python3
#
# [344] Reverse String
#

# @lc code=start
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        LENGTH = len(s)
        l = 0
        r = LENGTH - 1

        while l < r:
            s[l], s[r] = s[r], s[l]
            l, r = l + 1, r - 1


# @lc code=end

