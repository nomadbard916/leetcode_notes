#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        LENGTH = len(nums)
        if LENGTH == 0:
            return 0

        slow = 0
        fast = 1

        while fast < LENGTH:
            if nums[fast] != nums[slow]:
                slow += 1
                # we only want the total count in result,
                # not caring about what exactly the values are
                nums[slow] = nums[fast]

            fast += 1

        return slow + 1


# @lc code=end
