#
# @lc app=leetcode id=118 lang=python3
#
# [118] Pascal's Triangle
#

# @lc code=start
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []

        for n in range(numRows):  # nth layer
            # prepopulate 1 into triangle,
            # so it's certain the first and the last element will be 1
            triangle.append([1] * (n + 1))

            for i in range(1, n):  # deal with anything in between
                triangle[n][i] = triangle[n - 1][i - 1] + triangle[n - 1][i]

        return triangle


# @lc code=end

