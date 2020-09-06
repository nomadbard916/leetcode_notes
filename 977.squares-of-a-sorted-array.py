#
# @lc app=leetcode id=977 lang=python3
#
# [977] Squares of a Sorted Array
#

# @lc code=start
class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        unsorted = [x ** 2 for x in A]

        return sorted(unsorted)


# @lc code=end

