from collections import defaultdict

#
# @lc app=leetcode id=287 lang=python3
#
# [287] Find the Duplicate Number
#

# @lc code=start
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        seen = defaultdict(int)

        for num in nums:
            if num not in seen:
                seen[num] += 1
            else:
                return num


# @lc code=end

