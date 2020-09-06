#
# @lc app=leetcode id=80 lang=python3
#
# [80] Remove Duplicates from Sorted Array II
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # ordered: two pointer (implicit)

        i = 0
        for n in nums:
            if i < 2 or n != nums[i - 2]:
                nums[i] = n
                i += 1
        return i


# @lc code=end

