#
# @lc app=leetcode id=227 lang=python3
# @lcpr version=30305
#
# [227] Basic Calculator II
#

# @lc code=start
from typing import List


class Solution:
    def calculate(self, s: str) -> int:
        """
        * nouns and verbs
        string: non-negative integer and operator, seperator space
        expression, valid
        evaluate
        return
        value: 32-bit integer
        integer division: truncate
        assume valid
        intermediate result: range of [-2^31, 2^31-1]

        * pattern kws
        stack

        * constraints
        all intermediate result in [-2^31, 2^31-1]
        integer division truncate toward zero
        don't use any built-in for evaluation like eval()
        len range: 1<= len <= 3*10^5
        s only integers and operators
        s must be valid
        all integers are non-negative, range: [0, 2^31-1]
        answer must be 32-bit integer

        * kw-algo mapping
        just stack?

        * mental categories
        ?

        * tricky kws:
        */ must go before +-
        double figure

        * problem specific kws
        ?


        """

        # I can't think of the shape?

        if not s:
            return 0

        stack: List[int] = []
        current_num = 0
        # default
        operation = "+"

        OPERATORS = "+-*/"

        LAST_INDEX = len(s) - 1

        # I don't think there's need to record index
        for i, char in enumerate(s):
            # don't skip space at the very beginning,
            # or you'll prevent the last number from being processed by skipping the last index check
            if char.isdigit():
                current_num = current_num * 10 + int(char)

            if char in OPERATORS or i == LAST_INDEX:
                if operation == "+":
                    stack.append(current_num)
                if operation == "-":
                    stack.append(-current_num)
                if operation == "*":
                    multiplied = stack.pop() * current_num
                    stack.append(multiplied)
                if operation == "/":
                    # it should truncate toward 0, so don't just use //,
                    # it's only correct for positive
                    divided = int(stack.pop() / current_num)
                    stack.append(divided)

                operation = char
                current_num = 0

        return sum(stack)

        # if not stack[-1]:
        #     stack.append(int(char))
        #     continue
        # stack.append(int(char))

        return 0


# @lc code=end


#
# @lcpr case=start
# "3+2*2"\n
# @lcpr case=end

# @lcpr case=start
# " 3/2 "\n
# @lcpr case=end

# @lcpr case=start
# " 3+5 / 2 "\n
# @lcpr case=end

#
