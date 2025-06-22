#
# @lc app=leetcode id=51 lang=python3
# @lcpr version=30104
#
# [51] N-Queens
#

# @lc code=start
from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # ! it's essentially a decision making problem with backtracking
        result = []

        # Track which columns and diagonals are under attack
        # Columns that have queens
        cols_attackable = set()
        # Positive diagonal (row - col = constant)
        diag_attackable_pos = set()
        # Negative diagonal (row + col = constant)
        diag2_attackable_neg = set()

        def backtrack(row: int, board: List[str]) -> None:
            """
            Recursively place queens row by row using backtracking.
            """
            # * ending condition: if we've placed queens in all rows, we found a solution
            if row == n:
                # Make a copy of the current board
                result.append(board[:])

            # * choice list: try placing a queen in each column of the current row
            for col in range(n):
                # * make choice
                # Check if this position is safe (not under attack). skip if under attack
                positive_diag_pos = row - col
                negative_diag_pos = row + col
                if (
                    col in cols_attackable
                    or positive_diag_pos in diag_attackable_pos
                    or negative_diag_pos in diag2_attackable_neg
                ):
                    continue

                # place the queen
                cols_attackable.add(col)
                diag_attackable_pos.add(row - col)
                diag2_attackable_neg.add(row + col)

                # create the row string with queen at position col
                row_str = "." * col + "Q" + "." * (n - col - 1)
                board.append(row_str)

                # * recursively solve for the next row
                backtrack(row + 1, board)

                # * cancel the decision: remove the queen and try next position
                cols_attackable.remove(col)
                diag_attackable_pos.remove(row - col)
                diag2_attackable_neg.remove(row + col)
                board.pop()

        backtrack(0, [])
        return result


# @lc code=end


#
# @lcpr case=start
# 4\n
# @lcpr case=end

# @lcpr case=start
# 1\n
# @lcpr case=end

#
