#
# @lc app=leetcode id=55 lang=python3
#
# [55] Jump Game
#

# @lc code=start
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # greedy
        reachable_index: int = 0

        for i, num in enumerate(nums):
            if i > reachable_index:
                return False

            current_reachable: int = i + num

            reachable_index = max(reachable_index, current_reachable)

        return True


# @lc code=end

