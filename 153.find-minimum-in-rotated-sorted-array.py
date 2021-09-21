#
# @lc app=leetcode id=153 lang=python3
#
# [153] Find Minimum in Rotated Sorted Array
#

# @lc code=start
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        # binary search
        length = len(nums)

        if length == 1:
            return nums[0]

        l, r = 0, length - 1

        # after rotation, l must be bigger than r, or l is guaranteed to be the ans.
        while nums[l] > nums[r]:
            mid = (l + r) // 2

            if nums[mid] == nums[l]:
                return nums[r]

            if nums[mid] > nums[l]:
                l = mid + 1
            elif nums[mid] < nums[l]:
                r = mid

        return nums[l]


# @lc code=end

