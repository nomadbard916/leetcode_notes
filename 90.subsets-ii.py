from typing import List

#
# @lc app=leetcode id=90 lang=python3
#
# [90] Subsets II
#

# @lc code=start
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []

        nums.sort()

        if not nums:
            return ans

        def backtrack(current_path=[], option_list=nums):
            if current_path not in ans:
                ans.append(current_path)

            for i, num in enumerate(option_list):
                if i > 0 and num == option_list[i - 1]:
                    continue

                updated_path = current_path + [num]
                updated_options = option_list[i + 1 :]

                backtrack(updated_path, updated_options)

        backtrack()

        return ans


# @lc code=end

