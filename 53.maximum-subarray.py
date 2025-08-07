#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # This is a classic dynamic programming problem solved efficiently using Kadane's Algorithm.
        if len(nums) == 0:
            return 0

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


# @lc code=end
