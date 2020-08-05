#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#

# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)

        seen = {}

        for num in nums:
            seen[num] = seen.get(num, 0) + 1

            if seen[num] > n / 2:
                return num


# @lc code=end

