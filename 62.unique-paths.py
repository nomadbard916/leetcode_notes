#
# @lc app=leetcode id=62 lang=python3
#
# [62] Unique Paths
#

# @lc code=start
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # tabulation
        table = [[0 for x in range(m)] for y in range(n)]

        # first row and column should all be 1
        for i in range(m):
            table[0][i] = 1

        for i in range(n):
            table[i][0] = 1

        # for the rest of grids
        for i in range(1, n):
            for j in range(1, m):
                table[i][j] = table[i - 1][j] + table[i][j - 1]

        return table[-1][-1]


# @lc code=end

