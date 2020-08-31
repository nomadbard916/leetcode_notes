#
# @lc app=leetcode id=62 lang=python3
#
# [62] Unique Paths
#

# @lc code=start
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # tabulation; mn is wrong here, see the description (7*3 mistaken to be n*m)
        table = [[0 for x in range(m)] for y in range(n)]

        for x in range(m):
            for y in range(n):
                # first row and column should all be 1
                if x == 0:
                    table[y][x] = 1
                elif y == 0:
                    table[y][x] = 1
                # every other grid should be the sum of (x-1, y), (x, y-1) following the restricted moving direction
                else:
                    table[y][x] = table[y - 1][x] + table[y][x - 1]

        return table[-1][-1]


# @lc code=end

