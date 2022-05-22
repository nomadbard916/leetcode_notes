from collections import defaultdict
from typing import List

#
# @lc app=leetcode id=287 lang=python3
#
# [287] Find the Duplicate Number
#


# @lc code=start
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # sol1, O(n)
        seen = defaultdict(int)

        for num in nums:
            if num not in seen:
                seen[num] += 1
            else:
                return num

        # sol2: abstract it to "linked list looping", O(n)
        # see also 142, and here's guaranteed to be duplicated
        # slow = nums[0]
        # fast = nums[nums[0]]
        # while slow != fast:
        #     fast = nums[nums[fast]]
        #     slow = nums[slow]
        # fast = 0
        # while slow != fast:
        #     fast = nums[fast]
        #     slow = nums[slow]
        # return fast

        # sol3: binary search


# @lc code=end
