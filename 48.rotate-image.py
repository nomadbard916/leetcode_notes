#
# @lc app=leetcode id=48 lang=python3
#
# [48] Rotate Image
#

# @lc code=start
from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        n = len(matrix)

        # Step 1: Transpose the matrix (swap elements across main diagonal)
        # Main diagonal goes from top-left to bottom-right
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # or we may call matrix.reverse() at the very beginning
        # calling later is more intuitive and easier to debug mentally,
        # plus transpose appears in many other matrix problems
        # Step 2: Reverse each row
        for i in range(n):
            matrix[i].reverse()

        # Time Complexity: O(n²) - we must visit every element once
        # Space Complexity: O(1) - only using constant extra space

        # * Matrix Transformations Pattern:

        # 90° counterclockwise: reverse rows → transpose
        # 180°: reverse rows → reverse columns
        # Mirror horizontally: reverse rows
        # Mirror vertically: reverse columns

        # * In-place Algorithm Techniques:

        # When you can't use extra space, look for mathematical patterns
        # Sometimes breaking complex operations into simpler ones helps
        # Consider cyclic swaps for rearranging elements


# @lc code=end
