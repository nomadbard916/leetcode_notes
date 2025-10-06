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
        rows: List[Set[str]] = [set() for _ in range(9)]
        cols: List[Set[str]] = [set() for _ in range(9)]
        boxes: List[Set[str]] = [set() for _ in range(9)]

        empty_cells: List[Tuple[int, int]] = []

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
            if cell_idx == len(empty_cells):
                return True

            r, c = empty_cells[cell_idx]
            box_idx = (r // 3) * 3 + (c // 3)

            for num in "123456789":
                if (
                    num not in rows[r]
                    and num not in cols[c]
                    and num not in boxes[box_idx]
                ):
                    board[r][c] = num
                    rows[r].add(num)
                    cols[c].add(num)
                    boxes[box_idx].add(num)

                    if backtrack(cell_idx + 1):
                        return True

                    board[r][c] = "."
                    rows[r].remove(num)
                    cols[c].remove(num)
                    boxes[box_idx].remove(num)
            return False

        backtrack(0)


# @lc code=end


#
# @lcpr case=start
# \n[["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]\n
# @lcpr case=end

#
