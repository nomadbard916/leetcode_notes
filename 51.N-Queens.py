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

        cols = set()
        diag1 = set()
        diag2 = set()

        def backtrack(row: int, board: List[str]) -> None:
            # * base case: if we've placed queens in all rows, we found a solution
            if row == n:
                result.append(board[:])

            for col in range(n):
                if col in cols or (row - col) in diag1 or (row + col) in diag2:
                    continue

                # place the queen
                cols.add(col)
                diag1.add(row - col)
                diag2.add(row + col)

                # create the row string with queen at position col
                row_str = "." * col + "Q" + "." * (n - col - 1)
                board.append(row_str)

                # recursively solve for the next row
                backtrack(row + 1, board)

                # cancel the decision: remove the queen and try next position
                cols.remove(col)
                diag1.remove(row - col)
                diag2.remove(row + col)
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
