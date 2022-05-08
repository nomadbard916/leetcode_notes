#
# @lc app=leetcode id=47 lang=python3
#
# [47] Permutations II
#

# @lc code=start
from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        perm_n = len(nums)
        ans = []

        if perm_n == 0:
            return ans

        nums.sort()

        def backtrack(current_path, option_list=nums):

            if len(current_path) == perm_n and current_path not in ans:
                ans.append(current_path)
                return

            for i, num in enumerate(option_list):
                # cut duplication here so there's no need to exclude already existed path in ans for later layer of backtrack
                # if i > 0 and option_list[i] == option_list[i - 1]:
                #     continue

                updated_path = current_path + [num]
                updated_options = option_list[:i] + option_list[i + 1 :]

                backtrack(updated_path, updated_options)

        current_path = []
        backtrack(current_path)

        return ans


# @lc code=end
