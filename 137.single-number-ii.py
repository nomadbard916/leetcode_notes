from collections import Counter

#
# @lc app=leetcode id=137 lang=python3
#
# [137] Single Number II
#

# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        counter = Counter(nums)

        for n, count in counter.items():
            if count == 1:
                return n


# @lc code=end

