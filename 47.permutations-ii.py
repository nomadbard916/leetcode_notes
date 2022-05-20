#
# @lc app=leetcode id=47 lang=python3
#
# [47] Permutations II
#

# @lc code=start
from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        PERM_N = len(nums)
        ans = []

        if PERM_N == 0:
            return ans

        def backtrack(current_path: list, option_list: list):
            # ending condition
            if len(current_path) == PERM_N and current_path not in ans:
                ans.append(current_path)
                return

            for i, num in enumerate(option_list):
                updated_path = current_path + [num]
                # cut duplication here,
                # so there's no need to exclude already existed path in ans
                # for later layer of backtrack
                updated_options = option_list[:i] + option_list[i + 1 :]

                backtrack(updated_path, updated_options)

        backtrack([], nums)

        return ans


# @lc code=end
