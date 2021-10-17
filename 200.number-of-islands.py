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
        length = len(grid)
        width = len(grid[0])

        def dfs(grid, i, j):
            grid[i][j] = "0"
            # up
            if i - 1 >= 0 and grid[i - 1][j] == "1":
                dfs(grid, i - 1, j)
            # down
            if i + 1 < length and grid[i + 1][j] == "1":
                dfs(grid, i + 1, j)
            # left
            if j - 1 >= 0 and grid[i][j - 1] == "1":
                dfs(grid, i, j - 1)
            # right
            if j + 1 < width and grid[i][j + 1] == "1":
                dfs(grid, i, j + 1)

        counter = 0
        for i in range(length):
            for j in range(width):
                if grid[i][j] == "1":
                    counter += 1
                    dfs(grid, i, j)

        return counter


# @lc code=end

