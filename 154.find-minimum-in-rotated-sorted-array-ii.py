#
# @lc app=leetcode id=154 lang=python3
#
# [154] Find Minimum in Rotated Sorted Array II
#

# @lc code=start
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        # binary search
        l, r = 0, len(nums) - 1

        while l < r:
            mid = (l + r) // 2

            if nums[mid] < nums[r]:
                r = mid
            elif nums[mid] > nums[r]:
                l = mid + 1
            # consider when mid exactly equals r
            else:
                r -= 1

        return nums[l]


# @lc code=end

