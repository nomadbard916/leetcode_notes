from math import sqrt

#
# @lc app=leetcode id=69 lang=python3
#
# [69] Sqrt(x)
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        # cf. # 34
        # [l, r)
        l, r = 0, x + 1

        while l < r:
            mid = (l + r) // 2

            if mid ** 2 == x:
                return mid
            elif mid ** 2 < x:
                l = mid + 1
            else:
                r = mid

        return l - 1


# @lc code=end

