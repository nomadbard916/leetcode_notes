#
# @lc app=leetcode id=62 lang=python3
#
# [62] Unique Paths
#

# @lc code=start
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # ! sol1: 2D DP
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

        # ! sol2: 1D DP, space optimized with state compression
        # Use only one row to store the results
        # dp[j] represents the number of ways to reach column j in the current row
        # so we only need to reuse the same array
        dp = [1] * n

        # Process each row starting from the second row
        for y in range(1, m):
            for x in range(1, n):
                # Before updating dp[j] for the current row:
                # dp[j] still contains the value from the previous row (what we need for "above")
                # dp[j-1] contains the updated value from the current row (what we need for "left")
                dp[x] = dp[x] + dp[x - 1]

        return dp[n - 1]

        # complexities
        # Time: O(m × n) - same number of operations
        # Space: O(n) - only store one row

        # ! sol3: math
        """
        Mathematical approach using combinations.

        To reach (m-1, n-1) from (0, 0), we need exactly:
        - (m-1) down moves
        - (n-1) right moves
        - Total moves = (m-1) + (n-1) = m + n - 2

        The problem becomes: "In how many ways can we choose (m-1) positions
        for down moves out of (m + n - 2) total moves?"

        This is a combination problem: C(m + n - 2, m - 1) = C(m + n - 2, n - 1)
        """
        from math import comb

        return comb(m + n - 2, m - 1)


# @lc code=end
