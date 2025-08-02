#
# @lc app=leetcode id=278 lang=python3
#
# [278] First Bad Version
#

# @lc code=start
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):


class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1

        l, r = 1, n

        # sol1
        while l < r:
            mid = (l + r) // 2
            if isBadVersion(mid):
                r = mid
            else:
                l = mid + 1
        # when l == r, it is the first bad version
        return l


# @lc code=end
