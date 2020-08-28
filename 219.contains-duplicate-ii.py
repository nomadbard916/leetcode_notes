from collections import defaultdict

#
# @lc app=leetcode id=219 lang=python3
#
# [219] Contains Duplicate II
#

# @lc code=start
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        value_index = {}

        for i, num in enumerate(nums):
            # only need to compare two nearest indexes for current and previous
            if num in value_index and i - value_index[num] <= k:
                return True
            else:
                value_index[num] = i

        return False


# @lc code=end

