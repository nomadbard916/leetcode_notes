#
# @lc app=leetcode id=221 lang=python3
# @lcpr version=30305
#
# [221] Maximal Square
#

# @lc code=start

from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        """
        * nouns and verbs
        - m x n matrix, 0 and 1
        - largest "square" contain only 1
        - area
        * pattern kws
        - DFS?
        - overlapping problems?
        * constraint kws
        1 <= m, n <= 300
        the largest area can only be (smaller of m or n) ^2
        * map kws to algo concepts
        - overlapping? => DP?
        * build mental model
        indexing  cell?
        hash map to record each cell, record: (is_1, biggest area)
        check upper-left cells repeatedly, more specifically: up, left, upper-left
        check the upper-left diagonal cell
        * tricky kws
        * pattern specific kws
        * impl
        """
        # ! sol1: 2D DP
        # tracking side instead of area
        if not matrix or not matrix[0]:
            return 0
        m = len(matrix)
        n = len(matrix[0])
        max_side = 0

        dp: List[List[int]] = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '0':
                    continue

                # first row or col: at most a 1x1 square
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:

                    top = dp[i-1][j]
                    left = dp[i][j-1]
                    diagonal = dp[i-1][j-1]

                    dp[i][j]= min(top, left, diagonal) +1
                max_side = max(max_side, dp[i][j])



        return max_side ** 2

# @lc code=end



#
# @lcpr case=start
# [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]\n
# @lcpr case=end

# @lcpr case=start
# [["0","1"],["1","0"]]\n
# @lcpr case=end

# @lcpr case=start
# [["0"]]\n
# @lcpr case=end

#

