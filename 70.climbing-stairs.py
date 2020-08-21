#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1

        table = [0] * (n + 1)

        for i in range(1, n + 1):
            if i == 1 or i == 2:
                table[i] = i
            else:
                table[i] = table[i - 1] + table[i - 2]

        return table[-1]


# @lc code=end

