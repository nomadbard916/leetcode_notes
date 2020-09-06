#
# @lc app=leetcode id=394 lang=python3
#
# [394] Decode String
#

# @lc code=start
class Solution:
    def decodeString(self, s: str) -> str:
        # binary state change with sequence -> queue or stack
        # especially for brackets (think of stack immediately)

        current_multiplier: int = 0
        current_str = ""

        stack = []

        for char in s:
            if char == "[":
                stack.append(current_multiplier)
                stack.append(current_str)

                # clear the temp string and multiplier
                current_str = ""
                current_multiplier = 0

            elif char == "]":
                prev_string = stack.pop()
                recent_multiplier = stack.pop()

                current_str = prev_string + current_str * recent_multiplier

            elif char.isdigit():
                # consider more then 1 digit together
                current_multiplier = current_multiplier * 10 + int(char)

            else:  # must be alpha
                current_str += char

        return current_str


# @lc code=end

