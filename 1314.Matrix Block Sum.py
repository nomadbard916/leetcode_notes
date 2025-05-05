#
# @lc app=leetcode id=1314 lang=python3
# @lcpr version=30104
#
# [1314] Matrix Block Sum
#

# @lc code=start
from typing import List


class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        # sol 1: it's pretty much like 304 with padding prefix sum matrix
        # Explanation on integral image:
        # Here we use the technique of integral image, which is introduced to speed up block computation.
        # Also, this technique is practical and common in the field of matrix operation and image processing such as filtering and feature extraction.
        # Block sum formula on integral image. Block-sum of red rectangle = block-sum of D - block-sum of B - block-sum of C + block-sum of A
        m = len(mat)
        n = len(mat[0])

        integral = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m):
            for j in range(n):
                integral[i + 1][j + 1] = (
                    mat[i][j] + integral[i][j + 1] + integral[i + 1][j] - integral[i][j]
                )

        result = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                r1 = max(0, i - k)
                c1 = max(0, j - k)
                r2 = min(m - 1, i + k)
                c2 = min(n - 1, j + k)

                result[i][j] = (
                    integral[r2 + 1][c2 + 1]
                    - integral[r2 + 1][c1]
                    - integral[r1][c2 + 1]
                    + integral[r1][c1]
                )

        return result

        # sol2, but time complexity seems problematic and the structure is not clean enough
        m = len(mat)
        n = len(mat[0])
        answer = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                block_sum = 0
                for r in range(max(0, i - k), min(m, i + k + 1)):
                    for c in range(max(0, j - k), min(n, j + k + 1)):
                        block_sum += mat[r][c]
                answer[i][j] = block_sum
        return answer


# @lc code=end


#
# @lcpr case=start
# [[1,2,3],[4,5,6],[7,8,9]]\n1\n
# @lcpr case=end

# @lcpr case=start
# [[1,2,3],[4,5,6],[7,8,9]]\n2\n
# @lcpr case=end

#
