#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#

# @lc code=start
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # look for first digit in digits, look up possible letters
        # then look for next digits recursively, and check if letter combinations match answer

        ans_container = []
        ans_length = len(digits)

        # sanity check immediately
        if ans_length == 0:
            return ans_container

        dl_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        def backtrack(current_path: str = "", current_index: int = 0):
            # ending condition: out of bound
            if current_index > ans_length:
                return
            # ending condition: current path is one of the answers
            if len(current_path) == ans_length:
                ans_container.append(current_path)
                return

            # try to make option list
            current_digit = digits[current_index]
            current_letters = dl_map[current_digit]

            for letter in current_letters:
                # make decision: update visited path
                updated_path = current_path + letter
                backtrack(updated_path, current_index + 1)

        backtrack()

        return ans_container


# @lc code=end

