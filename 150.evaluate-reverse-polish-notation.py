#
# @lc app=leetcode id=150 lang=python3
#
# [150] Evaluate Reverse Polish Notation
#

# @lc code=start
from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            # put only numbers into stack
            if token not in ["+", "-", "*", "/"]:
                stack.append(int(token))
                continue

            # take numbers in pair, waiting to process with immediate operator
            a = stack.pop()
            b = stack.pop()

            if token == "+":
                stack.append(a + b)
            if token == "-":
                stack.append(b - a)
            if token == "*":
                stack.append(a * b)
            if token == "/":
                if a * b > 0:
                    stack.append(b // a)
                else:
                    # in Python, (-1)/2=-1
                    stack.append(-((-b) // a))

        return stack.pop()


# @lc code=end
