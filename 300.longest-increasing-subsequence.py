#
# @lc app=leetcode id=300 lang=python3
#
# [300] Longest Increasing Subsequence
#

# @lc code=start
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # dynamic programming

        length = len(nums)
        # initialize each position with max value at least 1
        dp = [1] * length

        for i in range(0, length):
            current_longest_num = 1
            # check if num[i] can be chained after each previous number
            # length +=1 if nums[i] can be chained
            for j in range(0, i):
                if nums[i] > nums[j]:
                    current_longest_num = max(current_longest_num, dp[j] + 1)
            dp[i] = current_longest_num

        return max(dp)


# @lc code=end

