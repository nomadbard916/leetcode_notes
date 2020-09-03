#
# @lc app=leetcode id=77 lang=python3
#
# [77] Combinations
#

# @lc code=start
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = list(range(1, n + 1))
        ans = []

        def backtrack(current_path=[], option_list=nums):
            if len(current_path) == k:
                ans.append(current_path)
                return

            for i in range(len(option_list)):
                updated_path = current_path + [option_list[i]]
                updated_option = option_list[i + 1 :]

                backtrack(updated_path, updated_option)

        backtrack()

        return ans


# @lc code=end

