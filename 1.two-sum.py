#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        m = {}

        for i, num in enumerate(nums):
            complement = target - num

            if complement not in m:
                m[num] = i

            else:
                return [i, m[complement]]


# @lc code=end

