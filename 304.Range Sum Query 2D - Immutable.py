#
# @lc app=leetcode id=304 lang=python3
# @lcpr version=30104
#
# [304] Range Sum Query 2D - Immutable
#

# @lc code=start
from typing import List


class NumMatrix:
    """
    NumMatrix supports efficient sum queries over a 2D matrix using a 2D prefix sum (summed-area table).
    """

    # ! any matrix can be calculated by bigger matrixes starting from (0,0)
    # let's say the matrix to be (ul, ur, dl, dr), then its sum:
    # (0,0)~(dl, dr) - (0,0)~(0,l)~(d,0) - (0,0)~(0,u)~(r,0) + (0,0)~(l,0)~(0,u)

    def __init__(self, matrix: List[List[int]]):
        # Dimensions of the input matrix
        rows = len(matrix)
        cols = len(matrix[0]) if rows > 0 else 0

        if rows == 0 or cols == 0:
            return

        # create a (rows +1) x (cols +1 ) DP table initialized to 0
        # dp[i][j] stores the sum of the submatrix from (0,0) to (i-1,j-1)
        self.dp = [[0] * (cols + 1) for _ in range(rows + 1)]

        # build the prefix sum table
        for r in range(rows):
            for c in range(cols):
                # Current value + sum above + sum left - sum above-left (to avoid double-count)
                self.dp[r + 1][c + 1] = (
                    matrix[r][c] + self.dp[r][c + 1] + self.dp[r + 1][c] - self.dp[r][c]
                )

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        """
        Return the sum of the elements inside the rectangle
        defined by its upper left (row1, col1) and lower right (row2, col2) corners (inclusive).

        Using the inclusion-exclusion principle on the prefix sum table:
        sumRegion = dp[r2+1][c2+1]
                    - dp[row1][c2+1]     (remove area above)
                    - dp[r2+1][col1]     (remove area left)
                    + dp[row1][col1]     (add back overlap)
        """

        # Shift indices by 1 to account for the extra padding in dp
        r2, c2 = row2 + 1, col2 + 1
        r1, c1 = row1, col1
        return self.dp[r2][c2] - self.dp[r1][c2] - self.dp[r2][c1] + self.dp[r1][c1]

    #     Time - O(m * n) - for the constructor
    # Space - O(m * n) - for storing the prefix sum array


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
# @lc code=end
