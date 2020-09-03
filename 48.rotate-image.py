#
# @lc app=leetcode id=48 lang=python3
#
# [48] Rotate Image
#

# @lc code=start
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        # https://blog.csdn.net/xie810005152/article/details/90339964

        matrix[:] = list(zip(*matrix[::-1]))

        # sol2:
        # matrix.reverse()
        # for i in range(len(matrix)):
        #     for j in range(i):
        #         matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


# @lc code=end

