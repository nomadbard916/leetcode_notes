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

        while l <= r:
            mid = (l + r) // 2
            if isBadVersion(mid):
                # sanity check
                if mid == 1 or (mid - 1 >= 1 and not isBadVersion(mid - 1)):
                    return mid

                r = mid - 1
            else:
                l = mid + 1
                # l cannot be bad, otherwise all versions afterward will be bad either


# @lc code=end

