#
# @lc app=leetcode id=275 lang=python3
#
# [275] H-Index II
#

# @lc code=start
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # sorted version of 274 h-index
        # don't sort again as it as already sorted ascending
        # binary search, much faster with O(nlog(n))

        n = len(citations)
        # set initial states
        l, r = 0, n - 1
        H = 0

        while l <= r:
            mid = l + (r - l) // 2

            H = max(H, min(citations[mid], n - mid))
            if citations[mid] < n - mid:
                l = mid + 1
            else:
                r = mid - 1

        return H


# @lc code=end

