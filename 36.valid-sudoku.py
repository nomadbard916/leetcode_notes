#
# @lc app=leetcode id=36 lang=python3
#
# [36] Valid Sudoku
#

# @lc code=start
from collections import defaultdict
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols_seen_nums = defaultdict(set)
        rows_seen_nums = defaultdict(set)
        matrixes_seen_nums = defaultdict(set)

        # every iteration goes 0..8, so we can just extract it beforehand
        matrix_range_iter = range(9)
        for i in matrix_range_iter:
            for j in matrix_range_iter:
                current_num = board[i][j]
                if current_num == ".":
                    continue

                if current_num in cols_seen_nums[j]:
                    return False
                cols_seen_nums[j].add(current_num)

                if current_num in rows_seen_nums[i]:
                    return False
                rows_seen_nums[i].add(current_num)

                # multiply by 10 to avoid key duplication.
                # actually any multiplier >=3 can do the trick.
                current_matrix_key: int = (i // 3) * 10 + j // 3
                if current_num in matrixes_seen_nums[current_matrix_key]:
                    return False
                matrixes_seen_nums[current_matrix_key].add(current_num)

        return True
        # sol2: tabulation from the very beginning
        # disadvantage: using list is counterintuitive when fetching value by index
        # matrix_range_iter = range(9)

        # row_tab: list = [[False] * 9 for _ in matrix_range_iter]
        # col_tab: list = [[False] * 9 for _ in matrix_range_iter]
        # matrix_tab: list = [[False] * 9 for _ in matrix_range_iter]

        # # iterate through every row & col
        # for i in matrix_range_iter:
        #     for j in matrix_range_iter:
        #         current_num = board[i][j]
        #         if current_num == ".":
        #             continue

        #         num_index = int(current_num) - 1
        #         matrix_index = i // 3 * 3 + j // 3

        #         element_exists = (
        #             row_tab[j][num_index]
        #             or col_tab[i][num_index]
        #             or matrix_tab[matrix_index][num_index]
        #         )

        #         if element_exists:
        #             return False

        #         row_tab[j][num_index] = True
        #         col_tab[i][num_index] = True
        #         matrix_tab[matrix_index][num_index] = True

        # return True


# @lc code=end
