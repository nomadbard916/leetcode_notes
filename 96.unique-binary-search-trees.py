#
# @lc app=leetcode id=96 lang=python3
#
# [96] Unique Binary Search Trees
#

# @lc code=start
class Solution:
    memo = {
        # 0 is actually out of range, but DP equilibrium needs it
        0: 1,
        # put known values into memo first
        1: 1,
        2: 2,
        3: 5,
    }

    def numTrees(self, n: int) -> int:
        if n in self.memo:
            return self.memo[n]

        ans = 0

        for i in range(1, n + 1):
            # any i in range can be root
            # take values smaller than i for left tree, bigger right tree
            # then multiply them for symmetry
            ans += self.numTrees(i - 1) * self.numTrees(n - i)

        self.memo[n] = ans

        return ans


# @lc code=end

