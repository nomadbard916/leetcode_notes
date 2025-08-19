from collections import Counter
from typing import List

#
# @lc app=leetcode id=75 lang=python3
#
# [75] Sort Colors
#

# @lc code=start


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # ! three-way partitioning
        # sol1: counting sort, space complexity O(N)

        counter = Counter(nums)

        for i, _ in enumerate(nums):
            if i < counter[0]:
                nums[i] = 0
            elif i < counter[0] + counter[1]:
                nums[i] = 1
            else:
                nums[i] = 2

        #  sol2: two pointers, one pass with O(nlog(n)) (T) / O(1) (S)
        # p0 as the righter most of 0, p2 as lefter most of 2
        # use i to start iteration, with initial p0, p2 = (0, len(nums)-1)
        # p0, i, p2 = 0, 0, len(nums) - 1
        # while i <= p2:
        #     if nums[i] == 0:
        #         # in-place swap
        #         nums[p0], nums[i] = nums[i], nums[p0]
        #         p0 += 1
        #         i += 1
        #     elif nums[i] == 2:
        #         nums[i], nums[p2] = nums[p2], nums[i]
        #         p2 -= 1
        #     else:
        #         i += 1


# @lc code=end
