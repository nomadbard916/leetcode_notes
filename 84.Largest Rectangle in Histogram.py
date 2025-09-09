#
# @lc app=leetcode id=84 lang=python3
# @lcpr version=30201
#
# [84] Largest Rectangle in Histogram
#

# @lc code=start
from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # !sol1
        # Approach: Use a stack to keep track of indices of bars in increasing order.
        # When we find a bar shorter than the top of stack, we calculate area with
        # the stack top as the smallest bar.
        stack = []
        max_area = 0

        n = len(heights)
        for i in range(n):
            while stack and heights[i] < heights[stack[-1]]:
                top_bar = stack.pop()
                height = heights[top_bar]

                width = i
                if stack:
                    width = i - stack[-1] - 1

                max_area = max(max_area, height * width)

            stack.append(i)

        while stack:
            height = heights[stack.pop()]

            width = n
            if stack:
                width = n - stack[-1] - 1

            max_area = max(max_area, height * width)

        return max_area

        # Time Complexity: O(n) - each bar is pushed and popped at most once
        # Space Complexity: O(n) - for the stack in worst case


# @lc code=end


#
# @lcpr case=start
# [2,1,5,6,2,3]\n
# @lcpr case=end

# @lcpr case=start
# [2,4]\n
# @lcpr case=end

#
