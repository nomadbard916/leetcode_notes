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
        #         Key Insight:
        # For any rectangle in the histogram, its height is determined by the shortest bar it contains.
        # So for each bar, we want to find the largest rectangle where that bar is the shortest.

        # !sol1
        # Approach: Use a stack to keep track of indices of bars in increasing order.
        # When we find a bar shorter than the top of stack, we calculate area with
        # the stack top as the smallest bar.
        stack = []  # Stack to store indices of histogram bars
        max_area = 0

        # Process each bar
        n = len(heights)
        for i in range(n):
            curr_bar = heights[i]
            while stack and curr_bar < heights[stack[-1]]:
                # Pop the top bar and calculate area with it as smallest bar
                top_bar = stack.pop()
                height = heights[top_bar]

                # Calculate width:
                # If stack is empty, width is current index (all bars to the left)
                # Otherwise, width is difference between current index and
                # the index after the new stack top
                width = i
                if stack:
                    width = i - stack[-1] - 1

                # Update maximum area
                max_area = max(max_area, height * width)

            stack.append(i)

        # Process remaining bars in stack
        while stack:
            curr_bar = stack.pop()
            height = heights[curr_bar]

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
