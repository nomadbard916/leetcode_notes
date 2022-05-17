#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#

# @lc code=start
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # find the first island piece 1 and update counter,
        # modify it as 0 then iterate 4-direction of it,
        # until there's no way to expend
        LENGTH = len(grid)
        WIDTH = len(grid[0])

        def dfs(grid, i, j):
            grid[i][j] = "0"

            upper_index = i - 1
            if upper_index >= 0 and grid[upper_index][j] == "1":
                dfs(grid, i - 1, j)
            lower_index = i + 1
            if lower_index < LENGTH and grid[lower_index][j] == "1":
                dfs(grid, i + 1, j)
            left_index = j - 1
            if left_index >= 0 and grid[i][left_index] == "1":
                dfs(grid, i, j - 1)
            right_index = j + 1
            if right_index < WIDTH and grid[i][right_index] == "1":
                dfs(grid, i, j + 1)

        counter = 0
        for i in range(LENGTH):
            for j in range(WIDTH):
                if grid[i][j] == "1":
                    counter += 1
                    dfs(grid, i, j)

        return counter


# @lc code=end

