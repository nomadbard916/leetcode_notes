#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow: int = 0
        fast: int = 1

        LENGTH: int = len(nums)

        while slow < fast and slow < LENGTH and fast < LENGTH:
            if nums[fast] != nums[slow]:
                slow += 1
                nums[slow] = nums[fast]

            fast += 1

        return slow + 1


# @lc code=end

