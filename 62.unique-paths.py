#
# @lc app=leetcode id=62 lang=python3
#
# [62] Unique Paths
#

# @lc code=start
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * n for _ in range(m)]

        # every other grid should be the sum of (x-1, y), (x, y-1) following the restricted moving direction
        for x in range(n):
            for y in range(m):
                # first row and column should all be 1
                if x == 0:
                    dp[y][x] = 1
                elif y == 0:
                    dp[y][x] = 1
                # every other grid should be the sum of (x-1, y), (x, y-1) following the restricted moving direction
                else:
                    dp[y][x] = dp[y - 1][x] + dp[y][x - 1]

        return dp[m - 1][n - 1]

        # complexities
        # Time: O(m × n) - fill every cell once
        # Space: O(m × n) - 2D array storage


# @lc code=end
