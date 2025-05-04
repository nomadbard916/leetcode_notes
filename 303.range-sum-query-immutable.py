#
# @lc app=leetcode id=303 lang=python3
#
# [303] Range Sum Query - Immutable
#

# @lc code=start
from typing import List


class NumArray:
    prefix_sum: List[int]

    def __init__(self, nums: List[int]):
        # construct prefix sum arr
        self.prefix_sum = [0] * (len(nums) + 1)
        for i in range(1, len(self.prefix_sum)):
            self.prefix_sum[i] = self.prefix_sum[i - 1] + nums[i - 1]

    def sumRange(self, i: int, j: int) -> int:
        return self.prefix_sum[j + 1] - self.prefix_sum[i]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
# @lc code=end
