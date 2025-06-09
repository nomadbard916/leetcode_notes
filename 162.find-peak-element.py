#
# @lc app=leetcode id=162 lang=python3
#
# [162] Find Peak Element
#

# @lc code=start
from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # ! compare with 852
        # O(log n) => binary search
        # need to check if it's going up or down, therefore mid and its helper
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            mid_helper = mid + 1

            if nums[mid] < nums[mid_helper]:
                l = mid_helper
            else:
                r = mid

        return l


# @lc code=end
