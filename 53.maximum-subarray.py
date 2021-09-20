#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        max_val = nums[0]
        current_sum = nums[0]

        for n in nums[1:]:
            if current_sum > 0:
                current_sum += n
            else:
                current_sum = n

            max_val = max(max_val, current_sum)

        return max_val


# @lc code=end

