#
# @lc app=leetcode id=73 lang=python3
#
# [73] Set Matrix Zeroes
#

# @lc code=start
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        R = len(matrix)
        C = len(matrix[0])

        rows_to_change, cols_to_change = set(), set()

        # iterate through the original matrix and find 0 elements,
        # then mark the rows and columns that are to be made zero
        for x in range(C):
            for y in range(R):
                if matrix[y][x] == 0:
                    rows_to_change.add(y)
                    cols_to_change.add(x)

        # Iterate over the array once again ,
        # update the elements using the data in rows and cols sets
        for x in range(C):
            for y in range(R):
                if x in cols_to_change or y in rows_to_change:
                    matrix[y][x] = 0


# @lc code=end

