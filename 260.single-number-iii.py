from collections import Counter

#
# @lc app=leetcode id=260 lang=python3
#
# [260] Single Number III
#

# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        counter = Counter(nums)

        return [num for num, count in counter.items() if count == 1]


# @lc code=end

