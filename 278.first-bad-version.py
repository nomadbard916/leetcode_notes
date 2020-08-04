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
        l = 1
        r = n

        while l < r:
            mid = (l + r) // 2
            if isBadVersion(mid):
                r = mid
                # r can be bad version as the single bad in this check
            else:
                l = mid + 1
                # l cannot be bad, otherwise all versions afterward will be bad either

        return l


# @lc code=end

