#
# @lc app=leetcode id=852 lang=python3
# @lcpr version=30104
#
# [852] Peak Index in a Mountain Array
#

# @lc code=start
from typing import List


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        # ! compare with 162
        # both close ended binary search
        l = 0
        r = len(arr) - 1

        # we can have ending condition l == r as answer is guaranteed
        while l < r:
            mid = (l + r) // 2
            if arr[mid] > arr[mid + 1]:
                # mid itself is the peak, or there's peak at its left
                r = mid
            else:
                # there's peak at right of mid
                l = mid + 1
        return l


# @lc code=end


#
# @lcpr case=start
# [0,1,0]\n
# @lcpr case=end

# @lcpr case=start
# [0,2,1,0]\n
# @lcpr case=end

# @lcpr case=start
# [0,10,5,2]\n
# @lcpr case=end

#
