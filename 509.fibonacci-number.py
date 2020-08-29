#
# @lc app=leetcode id=509 lang=python3
#
# [509] Fibonacci Number
#

# @lc code=start
class Solution:
    calculated = {0: 0, 1: 1}

    def fib(self, N: int) -> int:
        def memo(N) -> int:
            if N in self.calculated:
                return self.calculated[N]

            self.calculated[N] = memo(N - 1) + memo(N - 2)

            return memo(N)

        if N <= 1:
            return N

        return memo(N)


# @lc code=end

