#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#

# @lc code=start
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []

        # make sure each iteration won't see smaller element
        candidates.sort()

        # sanity check: the smallest one is already bigger than target
        if candidates[0] > target:
            return ans

        def backtrack(current_path: list, previous_c: int, current_sum: int):
            # sanity check: out of bound
            if current_sum > target:
                return

            # ending condition: combination found
            if current_sum == target:
                ans.append(current_path)
                return

            for current_c in candidates:
                # sanity check: out of bound.
                # no need to check candidate after it
                if current_c > target:
                    break

                # sanity check: avoid taking duplicated candidate
                if current_c < previous_c:
                    continue

                updated_path = current_path + [current_c]
                updated_sum = current_sum + current_c

                backtrack(updated_path, current_c, updated_sum)

        current_path = []
        previous_c = 0
        current_sum = 0
        backtrack(current_path, previous_c, current_sum)

        return ans


# @lc code=end
