#
# @lc app=leetcode id=221 lang=python3
# @lcpr version=30305
#
# [221] Maximal Square
#

# @lc code=start
from __future__ import annotations

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
        - overlapping? => 2D DP?
        * build mental model
        indexing  cell?
        hash map to record each cell, record: (is_1, biggest area)
        check upper-left cells repeatedly, more specifically: up, left, upper-left
        check the upper-left diagonal cell
        * tricky kws
        area... can be decomposed of sides multiplication
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

        # The composability problem
        # When you build a DP table, each cell needs to combine with its neighbors to produce a new answer.
        # The key question is: what value can I store that makes that combination simple?
        # Try storing area instead of side length and watch it break:
        # Neighbors storing area:
        #   top      = 4   (a 2×2 square)
        #   left     = 4   (a 2×2 square)
        #   diagonal = 4   (a 2×2 square)

        # What's the new area at the current cell?
        # You're stuck. To know whether you can extend, you need to know what shape produced that area.
        # A 4 could be a 2×2 square, or a 1×4 rectangle (if rectangles were allowed), or even a 4×1.
        # The area number alone doesn't tell you how many rows or columns the square occupies,
        # so you can't safely extend it.
        # Side length, by contrast, is unambiguous:
        # top = 2  →  guaranteed 2×2 square directly above
        # left = 2 →  guaranteed 2×2 square directly to the left
        # diag = 2 →  guaranteed 2×2 square at the corner

        # New side = min(2, 2, 2) + 1 = 3  ✓
        # One number tells you both width and height, because for a square they're always equal.
        # That's the geometric gift that squares give you — one dimension encodes both.

        # dp[i][j] stores the side length of the largest square
        # with its bottom-right corner at (i, j).
        dp: List[List[int]] = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                # If matrix[i][j] == '0', dp[i][j] stays 0 (no square ends here)
                if matrix[i][j] == '0':
                    continue

                # first row or col: at most a 1x1 square
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    # "Square" is the trap: a square means all three neighbors must agree — not just left and top.
                    # square directly above
                    top = dp[i-1][j]
                    # square directly to the left
                    left = dp[i][j-1]
                    # square at the diagonal
                    #  the diagonal is the bottleneck that enforces squareness.
                    diagonal = dp[i-1][j-1]

                    # All three must agree — the min is the bottleneck
                    # Why min and not max? Because we need all three sub-squares present, not the best one.
                    # max would let you pretend a bigger square exists when only one side supports it.
                    dp[i][j]= min(top, left, diagonal) +1
                max_side = max(max_side, dp[i][j])

        return max_side ** 2

        # Complexity
        # Approach| Time| Space
        # 2DDP | O(m × n) | O(m × n)
        # 1D rolling DP | O(m × n) | O(n)
        # In-place DP | O(m × n) | O(1) extra

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

