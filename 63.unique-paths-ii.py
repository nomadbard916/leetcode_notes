#
# @lc app=leetcode id=63 lang=python3
#
# [63] Unique Paths II
#

# @lc code=start
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])

        # tabulation
        # on setting default as 0, it covers obstacles already
        table = [[0 for x in range(n)] for y in range(m)]

        # sanity check: cannot begin at all if start from obstacle
        if obstacleGrid[0][0] == 1:
            return 0
        else:
            # set starting point manually
            table[0][0] = 1

        # for the rest of grids
        for y in range(m):
            for x in range(n):
                if obstacleGrid[y][x] == 0:
                    # pass starting point
                    if y == x == 0:
                        continue
                    else:
                        table[y][x] = table[y - 1][x] + table[y][x - 1]

        return table[-1][-1]


# @lc code=end

