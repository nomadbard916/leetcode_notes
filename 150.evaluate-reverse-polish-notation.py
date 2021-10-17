#
# @lc app=leetcode id=150 lang=python3
#
# [150] Evaluate Reverse Polish Notation
#

# @lc code=start
from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # think of Japanese, which puts verb after subject and object.
        stack = []

        for i in range(len(tokens)):
            current_token = tokens[i]

            # put numbers into stack
            if current_token not in ["+", "-", "*", "/"]:
                stack.append(int(current_token))
                continue

            a = stack.pop()
            b = stack.pop()

            if current_token == "+":
                stack.append(a + b)

            if current_token == "-":
                stack.append(b - a)

            if current_token == "*":
                stack.append(a * b)

            if current_token == "/":
                # in Python, (-1)/2=-1
                if a * b < 0:
                    stack.append(-((-b) // a))
                else:
                    stack.append(b // a)

        return stack.pop()


# @lc code=end

