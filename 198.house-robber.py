#
# @lc app=leetcode id=198 lang=python3
#
# [198] House Robber
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        length = len(nums)

        if length == 0:
            return 0

        # tabulation
        max_profit = [0] * length

        for i, num in enumerate(nums):
            if i == 0:
                max_profit[i] = num

            elif i == 1:
                max_profit[i] = max(nums[0], nums[1])

            else:
                max_profit[i] = max(nums[i] + max_profit[i - 2], max_profit[i - 1])

        return max_profit[-1]


# @lc code=end

