#
# @lc app=leetcode id=79 lang=python3
#
# [79] Word Search
#

# @lc code=start
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # search by x and y axis, and define depth and width
        # letters contain uppercase and lowercase

        def backtrack(y, x, current_string=""):
            # ending conditions: searching done, out of bound, visited or wrong target
            if current_string == word:  # when  visited path == word
                return True
            if x < 0 or x >= width or y < 0 or y >= height:  # out of bound
                return False

            # in order to make sure every option is only chosen once:
            # remember the original character, mark it traversed by changing it to '*', than change back when checking done
            current_option = board[y][x]

            # check if the current option is the exact match
            if current_option == "*":  # visited
                return False

            if (
                current_option != word[len(current_string)]
            ):  # wrong target, out of bound tackled in previous condition
                return False

            # if the current option matches, mark it visited by '*' then do backtracking
            # there's no need to check again options before * in backtrack() as the looping guarantees every option will be checked
            board[y][x] = "*"

            is_exist = (
                # backtracking by four directions with updated current string
                # if the new option matches, search by four directions recursively with  updated current_string
                backtrack(y, x + 1, current_string + current_option)
                or backtrack(y + 1, x, current_string + current_option)
                or backtrack(y, x - 1, current_string + current_option)
                or backtrack(y - 1, x, current_string + current_option)
            )

            # as the searching is done, recover the current position to previously saved value
            board[y][x] = current_option

            return is_exist

        # iterate through every option on board for the first match as starting point of recurion
        # then recursively search for each index in 'word' by backtrack()
        height = len(board)

        # sanity check:
        if height == 0:
            return False

        for y in range(height):
            width = len(board[y])  # as each row may not have the same col count
            for x in range(width):
                if backtrack(y, x):
                    return True

        return False


# @lc code=end

