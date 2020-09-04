#
# @lc app=leetcode id=1051 lang=python3
#
# [1051] Height Checker
#

# @lc code=start
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        target = sorted(heights)
        count = 0

        for i, h in enumerate(heights):
            if h != target[i]:
                count += 1

        return count


# @lc code=end

