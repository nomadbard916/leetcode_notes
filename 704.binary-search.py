#
# @lc app=leetcode id=704 lang=python3
#
# [704] Binary Search
#

# @lc code=start
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # ! it is just the template for binary search
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2

            mid_num: int = nums[mid]
            if mid_num == target:
                return mid
            if mid_num < target:
                l = mid + 1
            else:
                r = mid - 1

        return -1


# @lc code=end
