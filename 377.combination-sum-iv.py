#
# @lc app=leetcode id=377 lang=python3
#
# [377] Combination Sum IV
#

# @lc code=start
from typing import List


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # backtracking will definitely TLE => use DP
        # also reference to 70. Climbing Stairs

        # sanity check
        if min(nums) > target:
            return 0

        # state transition formula: dp[n] = dp[n] + dp[n-i]
        dp = [0] * (target + 1)
        dp[0] = 1

        # iterate through every step of dp, then check possibilities count of each num
        for i in range(1, target + 1):
            for num in nums:
                if i >= num:
                    dp[i] += dp[i - num]

        return dp[-1]


# @lc code=end

