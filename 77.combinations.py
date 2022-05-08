#
# @lc app=leetcode id=77 lang=python3
#
# [77] Combinations
#

# @lc code=start
from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = list(range(1, n + 1))
        ans = []

        def backtrack(current_path, option_list=nums):
            if len(current_path) == k:
                ans.append(current_path)
                return

            for i, num in enumerate(option_list):
                updated_path = current_path + [num]
                updated_option = option_list[i + 1 :]

                backtrack(updated_path, updated_option)

        current_path = []
        backtrack(current_path)

        return ans


# @lc code=end
