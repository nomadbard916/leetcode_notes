from collections import Counter

# @lc app=leetcode id=136 lang=python3
#
# [136] Single Number
#

# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        c = Counter(nums)

        for num, count in c.items():
            if count == 1:
                return num


# @lc code=end

