from collections import Counter
import functools
from typing import List

# @lc app=leetcode id=136 lang=python3
#
# [136] Single Number
#


# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # sol1: XOR with time: O(N), space O(1)
        # for every pair, num ^ num = 0
        # 0 ^ 0 = 0
        # so the only remaining single_num ^ 0 = u_num

        # initial state
        # single_num = 0

        # for num in nums:
        #     single_num ^= num
        # return single_num

        # sol2: XOR with python functools
        return functools.reduce(lambda x, y: x ^ y, nums)

        # sol3: intuitive, but less efficient with time: O(N), space: O(N)
        # c = Counter(nums)

        # for num, count in c.items():
        #     if count == 1:
        #         return num


# @lc code=end
