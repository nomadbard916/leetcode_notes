#
# @lc app=leetcode id=79 lang=python3
#
# [79] Word Search
#

# @lc code=start
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # search by x and y axis, and define depth and width
        # letters contain uppercase and lowercase

        def backtrack(y: int, x: int, current_string: str = ""):
            # * ending conditions: searching done, out of bound, visited or wrong target
            # when  visited path == word
            if current_string == word:
                return True
            # out of bound
            if x < 0 or x >= width or y < 0 or y >= height:
                return False

            # in order to make sure every option is only chosen once:
            # remember the original character, mark it traversed by changing it to '*', than change back when checking done
            current_option = board[y][x]

            # check if the current option is the exact match
            if current_option == "*":  # visited
                return False

            # wrong target, out of bound tackled in previous condition
            if current_option != word[len(current_string)]:
                return False

            # * if the current option matches, mark it visited by '*' then do backtracking
            # there's no need to check again options before * in backtrack() as the looping guarantees every option will be checked
            board[y][x] = "*"

            # * backtrack
            is_exist = (
                # backtracking by four directions with updated current string
                # if the new option matches, search by four directions recursively with  updated current_string
                backtrack(y, x + 1, current_string + current_option)
                or backtrack(y + 1, x, current_string + current_option)
                or backtrack(y, x - 1, current_string + current_option)
                or backtrack(y - 1, x, current_string + current_option)
            )

            # * cancel selection
            # as the searching is done, recover the current position to previously saved value
            board[y][x] = current_option

            return is_exist

        # iterate through every option on board for the first match as starting point of recurion
        # then recursively search for each index in 'word' by backtrack()
        height = len(board)
        width = len(board[0])

        for y in range(height):
            for x in range(width):
                if backtrack(y, x):
                    return True

        return False


# @lc code=end
