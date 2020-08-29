#
# @lc app=leetcode id=64 lang=python3
#
# [64] Minimum Path Sum
#

# @lc code=start
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        #  sanity check
        if len(grid) == 0 or len(grid[0]) == 0:
            return 0

        m, n = len(grid), len(grid[0])
        # don't make another container as grids are cumulative
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    before = 0
                elif i == 0:
                    before = grid[i][j - 1]
                elif j == 0:
                    before = grid[i - 1][j]
                else:
                    before = min(grid[i - 1][j], grid[i][j - 1])
                grid[i][j] = before + grid[i][j]
        return grid[m - 1][n - 1]


# @lc code=end

