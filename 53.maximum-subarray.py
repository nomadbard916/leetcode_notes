#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # !sol1: DP with Kadane's Algorithm. most efficient

        # Dynamic Programming has three essential characteristics, and this problem exhibits all of them:
        # - optimal substructure
        # If we know the maximum sum subarray ending at position i-1, we can optimally decide what to do at position i
        # The global maximum is the best among all "maximum subarrays ending at each position"
        # - overlapping subproblems
        # We repeatedly use the solution to "maximum subarray ending at position i-1"
        # to solve "maximum subarray ending at position i"
        # Without DP, we'd recalculate the same subproblems multiple times
        # - Memoization/Tabulation:
        # We store intermediate results (either in current_sum or explicit dp array)

        # Why This Works:
        # - If current_sum + nums[i] < nums[i], it means the previous subarray is dragging us down, so we start fresh
        # - We keep track of the maximum sum encountered so far, which gives us our answer

        # Think about it this way:
        # - Big Problem: "Find max subarray sum in entire array"
        # - Subproblem: "Find max subarray sum ending at position i"
        # - Relationship: To solve the big problem, solve all subproblems and take the maximum

        # At each position, we're building a decision tree:
        # Position i: Should I include nums[i] in my subarray?
        # ├─ YES: Then should I start fresh or extend?
        # │   ├─ Start fresh: cost = nums[i]
        # │   └─ Extend: cost = dp[i-1] + nums[i]
        # └─ NO: This doesn't make sense because we need subarrays ending at i

        # The beauty is that once you understand the DP nature here, you can tackle similar problems like:
        # - Maximum Product Subarray
        # - Maximum Sum Circular Subarray
        # - Best Time to Buy and Sell Stock
        # - House Robber
        if len(nums) == 0:
            return 0

        # * core of Kdane's algorithm:
        # I can keep accumulation from the beginning of array,
        # but once I've found a single bigger number than this current sum,
        # just get rid of the previous subarray totally,
        # and focus only on the rest part of the array.

        # Initialize with the first element
        max_sum = nums[0]
        current_sum = nums[0]

        # Iterate through the rest of the array
        for n in nums[1:]:
            # At each position, decide whether to:
            # 1. Start a new subarray from current element, or
            # 2. Extend the existing subarray by including current element
            current_sum = max(n, current_sum + n)

            # Update the maximum sum seen so far
            max_sum = max(max_sum, current_sum)

        return max_sum

        # Complexity Analysis:
        # - Time Complexity: O(n) - Single pass through the array
        # - Space Complexity: O(1) - Only using constant extra space


# @lc code=end
