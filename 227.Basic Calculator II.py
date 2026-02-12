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

        # Key Insights
        # 🎯 Core Strategy: "Stack as a Pending Operations Queue"
        # Mental Model (Audio-Oriented):
        # Think of the stack as a "waiting room" where numbers wait to be added together:
        # - When you see + or -: "Put this number in the waiting room" (push to stack)
        # - When you see * or /: "Call the last person out and calculate NOW" (pop, calculate, push back)
        # - At the end: "Sum everyone in the waiting room"

        # ! sol1: plain stack
        if not s:
            return 0

        stack: List[int] = []
        current_num = 0
        # Why we track "last operation" not "current operation":
        # - When we process a number, we apply the PREVIOUS operator to it
        # - This is because we don't know if the NEXT operator has higher precedence
        operation = "+"  # default

        OPERATORS = "+-*/"

        # I don't think there's need to record index
        for i, char in enumerate(s):
            # don't skip space at the very beginning,
            # or you'll prevent the last number from being processed by skipping the last index check
            if char.isdigit():
                current_num = current_num * 10 + int(char)

            # We need to process the last number even though there's no operator after it
            # That's why we check: if (we hit an operator) OR (we're at the end)
            if char in OPERATORS or i == len(s) - 1:
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

        # * Complexity Analysis
        # Stack Solution:
        # - Time Complexity: O(n)
        # Single pass through the string
        # Each character processed once
        # Stack operations (push/pop) are O(1)
        # - Space Complexity: O(n)
        # Stack can hold up to n/2 numbers in worst case
        # Example: "1+2+3+4+5" → stack holds all 5 numbers

        # Optimized Solution:
        # - Time Complexity: O(n)
        # Same single pass logic
        # - Space Complexity: O(1)
        # Only uses 3 variables: running_sum, last_value, current_number
        # Trade-off: Slightly more complex logic but constant space


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
