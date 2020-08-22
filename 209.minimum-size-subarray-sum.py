#
# @lc app=leetcode id=209 lang=python3
#
# [209] Minimum Size Subarray Sum
#

# @lc code=start
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        # two pointer: sliding window

        # there's no need to assign r here,
        # which will be done by range() as it needs to iterate through all the indexes of nums
        l = 0
        window_sum = 0

        int_INF = 2 << 32
        min_win_size = int_INF

        for r in range(len(nums)):
            window_sum += nums[r]

            while window_sum >= s:
                min_win_size = min(min_win_size, r - l + 1)
                window_sum -= nums[l]
                l += 1

        return min_win_size if min_win_size != int_INF else 0


# @lc code=end

