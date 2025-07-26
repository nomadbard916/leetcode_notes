#
# @lc app=leetcode id=416 lang=python3
# @lcpr version=30201
#
# [416] Partition Equal Subset Sum
#

# @lc code=start
from typing import List


class Solution:
    # see also: Target Sum 494, Last Stone Weight II 1049
    def canPartition(self, nums: List[int]) -> bool:
        # ! sol1: DP (bottom up)
        total_sum = sum(nums)

        # If total sum is odd, we can't partition into two equal subsets
        if total_sum % 2 != 0:
            return False

        target = total_sum // 2

        # DP approach: dp[i] represents whether sum i is achievable
        dp_target_num = [False] * (target + 1)
        dp_target_num[0] = True  # Sum of 0 is always achievable (empty subset)

        for num in nums:
            # Iterate backwards to avoid using the same number twice
            # Why iterate backwards?
            # If we go forwards, we might use the same number multiple times in one iteration.
            # For example, with num = 3, if we go forwards:
            # - dp[3] = True (using the number once)
            # - dp[6] = dp[6] or dp[3] = True (incorrectly using the number twice)
            for j in range(target, num - 1, -1):
                # Only update if we can make sum (j - num)
                if dp_target_num[j - num]:
                    dp_target_num[j] = True

        return dp_target_num[target]

        # Time Complexity: O(n × sum) where n is array length and sum is total sum
        # Space Complexity:
        # DP approach: O(sum)
        # Recursive approach: O(n × sum) for memoization + O(n) for recursion stack


# @lc code=end


#
# @lcpr case=start
# [1,5,11,5]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,5]\n
# @lcpr case=end

#
