#
# @lc app=leetcode id=410 lang=python3
# @lcpr version=30104
#
# [410] Split Array Largest Sum
#

# @lc code=start
from typing import List


class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        # min-possible maximum => right bound
        lo, hi = max(nums), sum(nums)
        while lo <= hi:
            mid = (lo + hi) // 2
            curr_arr_sum = 0
            curr_subarr_cnt = 1
            for num in nums:
                if curr_arr_sum + num <= mid:
                    curr_arr_sum += num
                else:
                    curr_arr_sum = num
                    curr_subarr_cnt += 1
            if curr_subarr_cnt <= k:
                hi = mid - 1
            else:
                lo = mid + 1
        # Need to add 1 since hi points to value just below answer
        return hi + 1


# @lc code=end


#
# @lcpr case=start
# [7,2,5,10,8]\n2\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4,5]\n2\n
# @lcpr case=end

#
