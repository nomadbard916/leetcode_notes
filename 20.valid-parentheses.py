#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isEqual(self, c1, c2):
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

        for character in s:
            if len(stack) != 0:
                # check the last item
                last_item = stack[-1]

                # the last item in stack and the current character must be the same
                if self.isEqual(last_item, character):
                    stack.pop()
                    continue

            stack.append(character)

        return len(stack) == 0


# @lc code=end
