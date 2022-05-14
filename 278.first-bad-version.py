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

        # sol2 is also good, but takes a bit more code.

        # while l <= r:
        #     mid = (l + r) // 2
        #     if isBadVersion(mid):
        #         # sanity check
        #         mid_is_first = mid == 1

        #         pre_mid = mid - 1
        #         pre_mid_not_bad = not isBadVersion(pre_mid)
        #         if mid_is_first or (pre_mid >= 1 and pre_mid_not_bad):
        #             return mid

        #         r = mid - 1
        #     else:
        #         l = mid + 1
        #         # l cannot be bad, otherwise all versions afterward will be bad either


# @lc code=end
