from collections import Counter

#
# @lc app=leetcode id=442 lang=python3
#
# [442] Find All Duplicates in an Array
#

# @lc code=start
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        return [no for no, count in Counter(nums).items() if count > 1]


# @lc code=end

