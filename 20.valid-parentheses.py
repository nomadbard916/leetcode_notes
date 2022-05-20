#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def are_pair(self, c1, c2):
        if c1 == "(" and c2 == ")":
            return True
        elif c1 == "[" and c2 == "]":
            return True
        elif c1 == "{" and c2 == "}":
            return True
        else:
            return False

    def isValid(self, s: str) -> bool:
        stack = []

        for current_char in s:
            if len(stack) != 0:
                last_item = stack[-1]
                if self.are_pair(last_item, current_char):
                    stack.pop()
                    continue

            stack.append(current_char)

        return len(stack) == 0


# @lc code=end
