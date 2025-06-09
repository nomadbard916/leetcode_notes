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
        l = 0
        r = len(arr) - 1

        while l < r:
            mid = (l + r) // 2
            if arr[mid] > arr[mid + 1]:
                r = mid
            else:
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
