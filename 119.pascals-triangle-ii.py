#
# @lc app=leetcode id=119 lang=python3
#
# [119] Pascal's Triangle II
#

# @lc code=start
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        # just follow 118, or it should use (comb, perm) in scipy.special
        triangle = []

        for n in range(rowIndex + 1):
            triangle.append([1] * (n + 1))

            for i in range(1, n):
                triangle[n][i] = triangle[n - 1][i - 1] + triangle[n - 1][i]

        return triangle[-1]


# @lc code=end

