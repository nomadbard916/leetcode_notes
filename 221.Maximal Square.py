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
        - overlapping?
        * constraint kws
        1 <= m, n <= 300
        the largest area can only be (smaller of m or n) ^2
        * map kws to algo concepts
        - overlapping? => DP?
        * build mental model
        indexing  cell?
        hash map to record each cell, record: (is_1, biggest area)
        check upper-left cells repeatedly
        check the upper-left diagonal cell
        * tricky kws
        * pattern specific kws
        * impl
        """
        ans = 0

        return ans

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

