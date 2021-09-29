#
# @lc app=leetcode id=40 lang=python3
#
# [40] Combination Sum II
#

# @lc code=start
from typing import List


class Solution:
    def backtrack(self, candidates, target, start_idx, ans, path):
        if target < 0:
            return

        length = len(candidates)
        if target == 0 and path not in ans:
            ans.append(path)
            return

        for i in range(start_idx, length):
            current_elm = candidates[i]
            if i > start_idx and current_elm == candidates[i - 1]:
                continue

            # sanity check: target exceeded
            if current_elm > target:
                return

            self.backtrack(
                candidates, target - current_elm, i + 1, ans, path + [current_elm]
            )

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []
        self.backtrack(candidates, target, 0, ans, [])

        return ans


# @lc code=end

