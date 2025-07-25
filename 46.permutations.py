#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#

# @lc code=start
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perm_n = len(nums)

        ans = []

        def backtrack(current_path):
            # * ending condition
            if len(current_path) == perm_n:
                ans.append(current_path)
                return

            # ! for each position, which balls can be put in?
            for num in nums:
                # * pruning condition
                if num in current_path:
                    continue

                # modify state
                updated_path = current_path + [num]

                backtrack(updated_path)

                # theres no need to recover state

        current_path = []
        backtrack(current_path)

        return ans

        # Time Complexity:
        # - There are `n!` permutations for a list of length `n`.
        # - For each permutation, the algorithm constructs a list of length `n`.
        # - So, the overall time complexity is **O(n × n!)**.

        # Space Complexity:
        # - The recursion stack can go up to `n` levels deep.
        # - The `ans` list stores all `n!` permutations, each of length `n`.
        # - So, the space complexity is **O(n × n!)**.

        # Summary:
        # - **Time:** O(n × n!)
        # - **Space:** O(n × n!)


# @lc code=end
