#
# @lc app=leetcode id=81 lang=python3
#
# [81] Search in Rotated Sorted Array II
#

# @lc code=start
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        # binary search
        l, r = 0, len(nums) - 1

        while l <= r:
            # deal with duplicates
            while l < r and nums[l] == nums[r]:
                l += 1

            mid = (l + r) // 2
            if nums[mid] == target:
                return True

            # ordered in range l~mid
            if nums[l] <= nums[mid]:
                # target falls in between
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            # ordered in range mid~r
            elif nums[mid] <= nums[r]:
                # target falls in between
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return False

        # sol2: simply do binary search
        # l, r = 0, len(nums) - 1
        # while l < r:
        #     m = (l + r) // 2
        #     if nums[m] < nums[r]:
        #         r = m
        #     elif nums[m] > nums[r]:
        #         l = m + 1
        #     else:
        #         r -= 1
        # return nums[l]


# @lc code=end

