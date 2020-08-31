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
        table = [[0 for x in range(n)] for y in range(m)]

        # can start if the beginning point has no obstacle;
        # ie. cannot start and set beginning to 0 if obstacle
        if obstacleGrid[0][0] == 0:
            table[0][0] = 1

        # for the rest of grids
        for y in range(m):
            for x in range(n):
                if obstacleGrid[y][x] == 1:
                    table[y][x] = 0
                else:
                    if y != 0:
                        table[y][x] += table[y - 1][x]
                    if x != 0:
                        table[y][x] += table[y][x - 1]

        return table[-1][-1]


# @lc code=end

