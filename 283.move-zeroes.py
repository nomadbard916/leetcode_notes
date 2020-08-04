#
# @lc app=leetcode id=283 lang=python3
#
# [283] Move Zeroes
#

# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        j = 0

        for num in nums:
            if num != 0:
                # move element to j, starting from the beginning of array
                nums[j] = num

                # goto next position to change numbers contiguously
                j += 1

        for i in range(j, len(nums)):
            # as every element until j is changed, ie there's j-1 non-zero elements
            # change everything to zero starting from position j
            nums[i] = 0


# @lc code=end

