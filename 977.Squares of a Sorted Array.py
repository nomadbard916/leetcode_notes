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
        l = 0
        r = n - 1

        # Fill result from the end (largest squares first)
        curr_pos = n - 1
        res = [0] * n

        # merge sorted lists with two pointers
        while l <= r:
            if abs(nums[l]) > abs(nums[r]):
                res[curr_pos] = nums[l] ** 2
                l += 1
            else:
                res[curr_pos] = nums[r] ** 2
                r -= 1
            curr_pos -= 1
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
