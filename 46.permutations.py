#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#

# @lc code=start
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # ! sol1: for each position, choose which ball to put in
        perm_n = len(nums)

        ans = []

        def backtrack(current_path):
            # * ending condition
            if len(current_path) == perm_n:
                ans.append(current_path)
                return

            # * for each position, which balls can be put in?
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

        # ! sol2: for each ball, choose which position to put in
        result = []
        path = [None] * len(nums)  # 預分配位置
        used_positions = [False] * len(nums)  # 記錄哪些位置被占用

        def backtrack(ball_index: int):
            if ball_index == len(nums):
                result.append(path[:])
                return

            current_ball = nums[ball_index]
            # 當前數字（球）可以放在哪個位置（盒子）？
            for pos in range(len(nums)):
                if used_positions[pos]:
                    continue

                path[pos] = current_ball
                used_positions[pos] = True
                backtrack(ball_index + 1)
                path[pos] = None
                used_positions[pos] = False

        backtrack(0)
        return result


# @lc code=end
