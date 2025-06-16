#
# @lc app=leetcode id=977 lang=python3
# @lcpr version=30104
#
# [977] Squares of a Sorted Array
#

# @lc code=start
from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # * it's essentially the extension to #88 and #21
        n = len(nums)
        # put two pointers at the biggest indexes of positive and negative child lists
        i = 0
        j = n - 1

        # the order is descending
        p = n - 1
        res = [0] * n

        # merge sorted lists with two pointers
        while i <= j:
            if abs(nums[i]) > abs(nums[j]):
                res[p] = nums[i] ** 2
                i += 1
            else:
                res[p] = nums[j] ** 2
                j -= 1
            p -= 1
        return res


# @lc code=end


#
# @lcpr case=start
# [-4,-1,0,3,10]\n
# @lcpr case=end

# @lcpr case=start
# [-7,-3,2,3,11]\n
# @lcpr case=end

#
