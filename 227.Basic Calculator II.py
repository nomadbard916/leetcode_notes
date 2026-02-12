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

        * problem specific kws
        ?


        """

        # I can't think of the shape?

        if not s:
            return 0

        stack: List[int] = []

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
