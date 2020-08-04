#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        # we cannot find the proper condition visually, therefore there's still need to try every possibility,
        # with DP and two pointer technique
        maxarea = 0
        l = 0
        r = len(height) - 1

        while l < r:
            current_area = min(height[l], height[r]) * (r - l)
            maxarea = max(maxarea, current_area)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return maxarea


# @lc code=end

