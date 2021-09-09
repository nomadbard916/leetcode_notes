#
# @lc app=leetcode id=45 lang=python3
#
# [45] Jump Game II
#

# @lc code=start
from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        # greedy
        # set initial values
        reachable_idx, idx_to_check, steps = 0, 0, 0

        # keep updating reachable_idx to cut possibilities
        while reachable_idx < len(nums) - 1:
            # record previously reached index to check possibilities of previous range of possibilities
            prev_farest_idx = reachable_idx

            while idx_to_check <= prev_farest_idx:
                # head directly to current farest,
                # then go back to each previous index to check possibilities
                new_reachable = idx_to_check + nums[idx_to_check]
                reachable_idx = max(reachable_idx, new_reachable)

                # increment until reaching previous farest
                idx_to_check += 1

            # actually jump after simulation done
            steps += 1

        return steps


# @lc code=end

