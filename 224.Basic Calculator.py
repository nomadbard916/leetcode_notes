#
# @lc app=leetcode id=224 lang=python3
# @lcpr version=30201
#
# [224] Basic Calculator
#

# @lc code=start
from typing import List


class Solution:
    # The stack allows us to "pause" our current calculation when we encounter parentheses,
    # solve the inner expression, and then "resume" with the saved state.
    def calculate(self, s: str) -> int:
        stack: List[int] = []
        result = 0
        number = 0
        sign = 1  # 1 for positive, -1 for negative

        for char in s:
            if char.isdigit():
                # build multi-digit numbers
                number = number * 10 + int(char)
            elif char in "+-":
                # prepare the current number with its sign
                result += sign * number
                number = 0  # reset for the next number
                sign = 1 if char == "+" else -1
            elif char == "(":
                # save current state before entering parenthes
                stack.append(result)
                stack.append(sign)
                # reset for the expression inside parenthes
                result = 0
                sign = 1
            elif char == ")":
                # complete current number and combine with saved state
                result += sign * number
                number = 0

                result *= stack.pop()  # Multiply by the sign before '('
                result += stack.pop()  # Add the result before '('

        # Don't forget the last number (no operator after it)
        return result + sign * number

        # Time and Space Complexity:
        # - Time Complexity: O(n) where n is the length of the string - we process each character once
        # - Space Complexity: O(n) in the worst case for the stack (deeply nested parentheses)


# @lc code=end


#
# @lcpr case=start
# "1 + 1"\n
# @lcpr case=end

# @lcpr case=start
# " 2-1 + 2 "\n
# @lcpr case=end

# @lcpr case=start
# "(1+(4+5+2)-3)+(6+8)"\n
# @lcpr case=end

#
