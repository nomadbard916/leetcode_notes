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
            # * ending condition:
            # all the nums are already considered
            if len(current_path) == perm_n:
                ans.append(current_path)
                return

            # for each position, which balls can be put in?
            for num in nums:
                # * pruning condition
                if num in current_path:
                    continue

                # * modify state
                updated_path = current_path + [num]

                backtrack(updated_path)

                # theres no need to recover state as the state keeps copied into arg

        backtrack([])

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

        # 哪種更適合？
        # 對於全排列問題，盒子選球更適合，原因：
        # - 符合直覺：我們習慣"從左到右填空"的思維
        # - 代碼簡潔：不需要預分配固定大小的數組
        # - 通用性強：容易擴展到部分排列、帶重複元素等情況
        # - 教學友好：大多數教程都採用這種方法

        # 球選盒子更適合的場景
        # 但是球選盒子在某些問題中反而更直觀：
        # - N皇后問題：每個皇后（球）選擇放在哪一行（盒子）
        # - 任務分配問題：每個任務（球）分配給哪個人（盒子）
        # - 圖著色問題：每個節點（球）選擇哪種顏色（盒子）


# @lc code=end
