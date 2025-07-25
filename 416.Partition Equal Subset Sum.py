#
# @lc app=leetcode id=416 lang=python3
# @lcpr version=30201
#
# [416] Partition Equal Subset Sum
#

# @lc code=start
from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # ! sol1: DP (bottom up)
        total_sum = sum(nums)

        # If total sum is odd, we can't partition into two equal subsets
        if total_sum % 2 != 0:
            return False

        target = total_sum // 2

        # DP approach: dp[i] represents whether sum i is achievable
        dp = [False] * (target + 1)
        dp[0] = True  # Sum of 0 is always achievable (empty subset)

        for num in nums:
            # Iterate backwards to avoid using the same number twice
            for j in range(target, num - 1, -1):
                # If we can make sum (j - num), then we can make sum j by adding num
                dp[j] = dp[j] or dp[j - num]

        return dp[target]


# @lc code=end


#
# @lcpr case=start
# [1,5,11,5]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,5]\n
# @lcpr case=end

#
