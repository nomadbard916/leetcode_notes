#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#

# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perm_n = len(nums)

        ans = []

        def backtrack(current_path):
            if len(current_path) == perm_n:
                ans.append(current_path)
                return

            for num in nums:
                if num in current_path:
                    continue
                else:
                    updated_path = current_path + [num]

                backtrack(updated_path)

        current_path = []
        backtrack(current_path)

        return ans


# @lc code=end
