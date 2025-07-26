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
        dp_target_num = [False] * (target + 1)  # target itself and dummy start 0
        dp_target_num[0] = True  # Sum of 0 is always achievable (empty subset)

        # * We Process One Number at a Time, But the DP Table Accumulates ALL Combinations
        # dp[j] represents whether sum j can be made using ANY combination of numbers processed so far,
        # not just the current number.
        for num in nums:
            # * Iterate backwards to avoid using the same number twice
            # We don't have to start from the last one! We can start from anywhere and go backwards, but we must go backwards to avoid dependency cycles.
            # Why iterate backwards?
            # If we go forwards, we might use the same number multiple times in one iteration.
            # For example, with num = 3, if we go forwards:
            # - dp[3] = True (using the number once)
            # - dp[6] = dp[6] or dp[3] = True (incorrectly using the number twice)
            # When processing number 3:
            # dp[3] depends on dp[0]
            # dp[6] depends on dp[3] ← Potential cycle here!
            # dp[9] depends on dp[6]
            # * Why We Choose target as Starting Point:
            # It's just optimal efficiency:
            # We want to find if dp[target] becomes True
            # Starting from target gives us the maximum chance to set dp[target] = True
            # Starting from middle means we might miss opportunities to reach the target
            # * The Real Pattern You're Seeing:
            # This isn't greedy behavior - it's topological ordering in disguise!
            # We're processing dependencies in an order that avoids cycles.
            # The "last to first" is just the most convenient way to ensure proper dependency ordering.
            for j in range(target, num - 1, -1):
                # Only update if we can make sum (j - num)
                # don't worry if the previous one has not set yet,
                # The Key Insight: dp[j-num] was determined in PREVIOUS iterations, not the current one!
                # * This single line is asking:
                # "For every sum we could make before, can we make a new sum by adding the current number?"
                # Why This Works:
                # - dp[j-num] = True means "some combination of previous numbers sums to j-num"
                # - We don't need to know WHICH combination - just that it exists
                # - Adding current number num gives us sum j
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
