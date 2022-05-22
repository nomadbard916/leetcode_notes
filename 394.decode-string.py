#
# @lc app=leetcode id=394 lang=python3
#
# [394] Decode String
#

# @lc code=start
class Solution:
    def decodeString(self, s: str) -> str:
        curr_multiplier: int = 0
        curr_str: str = ""

        stack = []

        for char in s:
            if char == "[":
                stack.append(curr_multiplier)
                stack.append(curr_str)

                # clear the temp string and multiplier
                curr_str = ""
                curr_multiplier = 0
            elif char == "]":
                # careful: when encountering '[', str is pushed on top of multiplier
                prev_str = stack.pop()
                recent_multiplier = stack.pop()

                curr_str = prev_str + curr_str * recent_multiplier

            elif char.isdigit():
                # considering digits >=10, every number adding need to x10,
                # e.g. 123 = 1 * 10 * 10 + 2*10 +3
                curr_multiplier = curr_multiplier * 10 + int(char)
            else:  # must be alpha, after all the above have been considered
                curr_str += char

        return curr_str


# @lc code=end
