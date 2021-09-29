#
# @lc app=leetcode id=216 lang=python3
#
# [216] Combination Sum III
#

# @lc code=start
from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []
        self.backtrack(range(1, 10), k, n, 0, ans, [])
        return ans

    def backtrack(self, nums, k, n, current_idx, ans, path):
        # if k < 0 or n < 0:
        #     return

        if k == 0 and n == 0:
            ans.append(path)
            return

        for i in range(current_idx, len(nums)):
            self.backtrack(nums, k - 1, n - nums[i], i + 1, ans, path + [nums[i]])


# @lc code=end

