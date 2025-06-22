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
        # ! N-Queens is fundamentally a brute-force  decision making approach, with backtracking as smart optimizations.
        # The "tricks" aren't just optimizations - they're what make the difference between:
        # - Theoretical algorithm: "Try everything"
        # - Practical algorithm: "Try everything intelligently"
        result = []

        # Track which columns and diagonals are under attack
        # Columns that have queens
        cols_attackable = set()
        # Positive Diagonals (↙ to ↗ direction) (row - col = constant)
        # These go from bottom-left to top-right.
        # Think of them as lines with a "positive slope" if you know basic math graphs.
        diag_attackable_pos = set()
        # Negative Diagonals (↖ to ↘ direction) (row + col = constant)
        # These go from top-left to bottom-right. Think of them as lines with a "negative slope".
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

    # Time and Space Complexity:
    # Time Complexity: O(N!) in the worst case
    # In each row, we have at most N choices
    # But with pruning, many branches are eliminated early
    # The actual complexity is much better than N! in practice

    # Space Complexity: O(N)
    # Recursion depth is N (one call per row)
    # Sets store at most N elements each
    # Board representation takes O(N) space


# @lc code=end


#
# @lcpr case=start
# 4\n
# @lcpr case=end

# @lcpr case=start
# 1\n
# @lcpr case=end

#
