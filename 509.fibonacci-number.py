#
# @lc app=leetcode id=509 lang=python3
#
# [509] Fibonacci Number
#

# @lc code=start
class Solution:
    calculated = {0: 0, 1: 1}

    def fib(self, N: int) -> int:
        if N in self.calculated:
            return self.calculated[N]

        self.calculated[N] = self.fib(N - 1) + self.fib(N - 2)

        return self.calculated[N]


# @lc code=end

