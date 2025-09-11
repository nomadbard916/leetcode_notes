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

        # Monotonic Stack Pattern:
        # This problem showcases the monotonic stack technique - maintaining stack elements in a specific order (increasing/decreasing). This pattern appears in many problems.

        # !sol1
        # Approach: Use a stack to keep track of indices of bars in increasing order.
        # When we find a bar shorter than the top of stack, we calculate area with
        # the stack top as the smallest bar.

        # Processing Logic:
        # When we encounter a bar shorter than the stack top,
        # it means we've found the right boundary for rectangles ending at the stack top
        # We pop from stack and calculate the area with the popped bar as the minimum height
        # The width is determined by the current index and the new stack top
        stack = []  # Stack to store indices of histogram bars
        max_area = 0

        n = len(heights)

        #     WHY TWO ROUNDS?
        # The key insight is that every bar needs both a LEFT and RIGHT boundary
        # to calculate its maximum possible rectangle area.
        # The stack algorithm finds these boundaries, but not all at once.
        # Round 1: Process each bar, handling cases where we find a "right boundary"
        # Round 2: Handle remaining bars that never found a right boundary
        # These bars can extend all the way to the end of the histogram

        # Think of it this way: each bar needs both left and right boundaries to
        # calculate its maximum rectangle. The stack helps us find these boundaries.

        # Round 1: Finding Right Boundaries
        # During the main loop, we're essentially asking: "What's the first bar to the right that's shorter than me?"
        # When we find such a bar, it becomes the right boundary for the taller bars in our stack.
        # Process each bar
        for i in range(n):
            # Key insight: when heights[i] < heights[stack[-1]],
            # bar i becomes the RIGHT BOUNDARY for rectangles ending at stack top
            curr_bar = heights[i]
            while stack and curr_bar < heights[stack[-1]]:
                # Pop the top bar and calculate area with it as smallest bar
                stacked_bar_i = stack.pop()
                height = heights[stacked_bar_i]

                # Calculate width: from left boundary to right boundary
                # Left boundary = element after current stack top (or start if empty)
                # Right boundary = current index i
                width = i
                if stack:
                    width = i - stack[-1] - 1

                # Update maximum area
                max_area = max(max_area, height * width)

            stack.append(i)

        # Round 2: Handling "Never-Found" Right Boundaries
        # Some bars never encounter a shorter bar to their right -
        # they can extend their rectangles all the way to the end of the histogram!
        # These remain in the stack after Round 1.
        # Process remaining bars in stack
        while stack:
            curr_bar = stack.pop()
            height = heights[curr_bar]

            # Right boundary is the end of array (len(heights))
            # Left boundary is after the current stack top (or start if empty)
            width = n
            if stack:
                width = n - stack[-1] - 1

            max_area = max(max_area, height * width)

        return max_area

        # Time Complexity: O(n) - each bar is pushed and popped at most once
        # Space Complexity: O(n) - for the stack in worst case

        # ! sol2: Alternative approach using sentinel values for cleaner code
        """
        Optimized version using sentinel values to avoid edge case handling.
        Add 0 at the beginning and end to handle edge cases elegantly.
        """
        # In the first solution, we needed two rounds because of edge cases:
        # Some bars never find a "right boundary"
        # Width calculation has special cases (empty stack vs non-empty)
        # We need different logic for "during loop" vs "after loop"

        # add sentinel values: 0 at start and end
        # The Left Sentinel (height = 0)
        # - Purpose: Ensures the stack is never empty during width calculation
        # - Effect: Every bar has a guaranteed "left boundary reference"
        # The Right Sentinel (height = 0)
        # - Purpose: Forces ALL remaining bars to be processed in the main loop
        # - Effect: Eliminates the need for a second round entirely
        heights = [0] + heights + [0]
        stack = []
        max_area = 0

        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                height = heights[stack.pop()]
                # With sentinels, width calculation becomes always the same formula
                # No special cases needed because:
                # - stack[-1] always exists (left sentinel guarantees non-empty stack)
                # - i is the right boundary (could be a real bar or right sentinel)
                # - The -1 accounts for exclusive boundaries
                width = i - stack[-1] - 1
                max_area = max(max_area, height * width)
            stack.append()

        return max_area


# @lc code=end


#
# @lcpr case=start
# [2,1,5,6,2,3]\n
# @lcpr case=end

# @lcpr case=start
# [2,4]\n
# @lcpr case=end

#
