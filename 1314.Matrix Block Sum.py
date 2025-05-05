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
        # it's pretty much like 304 with padding prefix sum matrix
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
