#
# @lc app=leetcode id=217 lang=python3
#
# [217] Contains Duplicate
#

# @lc code=start
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        no_dup = list(set(nums))

        return len(nums) != len(no_dup)


# @lc code=end

