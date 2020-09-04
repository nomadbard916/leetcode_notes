#
# @lc app=leetcode id=414 lang=python3
#
# [414] Third Maximum Number
#

# @lc code=start
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        num_no_dup = sorted(list(set(nums)))

        try:
            return num_no_dup[-3]
        except:
            return num_no_dup[-1]


# @lc code=end

