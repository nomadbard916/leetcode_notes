#
# @lc app=leetcode id=240 lang=python3
#
# [240] Search a 2D Matrix II
#

# @lc code=start
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # general case of 74 Search a 2D Matrix, so the code's the same


        # sanity check
        if not matrix or not matrix[0]:
            return False

        rows_count = len(matrix)
        cols_count = len(matrix[0])

        # start upper-right,
        # to just eliminate whole row when target is bigger than corner,
        # or move to left col when target smaller
        current_row, current_col = 0, cols_count -1


        while current_row < rows_count and current_col >= 0:
            if matrix[current_row][current_col] == target:
                return True
            elif matrix[current_row][current_col] < target:
                current_row +=1
            else:
                current_col -=1

        return False

# @lc code=end

