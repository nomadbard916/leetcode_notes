#
# @lc app=leetcode id=37 lang=python3
# @lcpr version=30201
#
# [37] Sudoku Solver
#

# @lc code=start
from typing import List, Set, Tuple


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # Backtracking is a systematic way to try all possibilities. Think of it as exploring a maze:
        # - Make a choice (place a number)
        # - If it leads to a dead end, backtrack (undo) and try another choice
        # - Continue until you find the exit (complete solution)

        # Track which numbers are already used in each row, column, and box
        # Using sets allows O(1) lookup to check if a number is already used.
        rows: List[Set[str]] = [set() for _ in range(9)]
        cols: List[Set[str]] = [set() for _ in range(9)]
        boxes: List[Set[str]] = [set() for _ in range(9)]

        # Collect all empty cells that need to be filled
        empty_cells: List[Tuple[int, int]] = []

        # Initialize the sets with existing numbers on the board
        for r in range(9):
            for c in range(9):
                if board[r][c] != ".":
                    num = board[r][c]
                    rows[r].add(num)
                    cols[c].add(num)
                    box_idx = (r // 3) * 3 + (c // 3)
                    boxes[box_idx].add(num)
                else:
                    empty_cells.append((r, c))

        def backtrack(cell_idx: int) -> bool:
            # Base case: all empty cells filled successfully
            if cell_idx == len(empty_cells):
                return True

            r, c = empty_cells[cell_idx]
            box_idx = (r // 3) * 3 + (c // 3)

            # Try each digit from '1' to '9'
            for num in "123456789":
                # Check if this number is valid (not in row, col, or box)
                if (
                    num not in rows[r]
                    and num not in cols[c]
                    and num not in boxes[box_idx]
                ):
                    board[r][c] = num
                    rows[r].add(num)
                    cols[c].add(num)
                    boxes[box_idx].add(num)

                    # Recursively try to fill the next cell
                    if backtrack(cell_idx + 1):
                        return True

                    # Backtrack: remove the number if it didn't lead to solution
                    board[r][c] = "."
                    rows[r].remove(num)
                    cols[c].remove(num)
                    boxes[box_idx].remove(num)

            # No valid number found for this cell
            return False

        backtrack(0)

        # Time Complexity: O(9^(n×n)) where n = 9

        # Worst case: try 9 options for each empty cell
        # In practice, much faster due to constraint pruning
        # Typical real Sudoku puzzles solve in milliseconds

        # Space Complexity: O(n²)

        # O(81) for the board itself
        # O(9) × 3 = O(27) for tracking sets
        # O(k) for recursion stack (k = number of empty cells, max 81)
        # Total: O(81) = O(1) since the board size is fixed


# @lc code=end


#
# @lcpr case=start
# \n[["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]\n
# @lcpr case=end

#
