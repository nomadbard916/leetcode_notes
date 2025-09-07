#
# @lc app=leetcode id=42 lang=python3
# @lcpr version=30201
#
# [42] Trapping Rain Water
#

# @lc code=start
from typing import List


class Solution:
    #     Why 42 Got "Hard" Label:
    # - Multiple Valid Approaches: Problem 42 has 4+ different solution approaches
    # (two pointers, DP, stack, brute force), which might make it seem more complex
    # - Visualization Difficulty: Some people find it harder to visualize
    # water "trapped above" vs water "contained between"
    # - Historical Context: It might have been one of the earlier problems on LeetCode
    # when the difficulty calibration wasn't as refined
    # - Edge Cases: Problem 42 has slightly more edge cases to handle (empty arrays, arrays with < 3 elements)
    def trap(self, height: List[int]) -> int:
        # ! sol1: two pointers (with two additional state-tracking pointers), also most efficient
        # The key insight is that the amount of water that can be trapped at any position
        # depends on the minimum of the maximum heights to its left and right

        # Step by step:
        # 1. Use two pointers from both ends
        # 2. Keep track of max heights seen so far from each side
        # 3. Always process the side with smaller height
        # 4. If current height < max height on that side, water is trapped
        LEN = len(height)
        if not height or LEN < 3:
            return 0

        l, r = 0, LEN - 1
        max_height_l, max_height_r = 0, 0
        water_trapped = 0

        while l < r:
            curr_height_l = height[l]
            curr_height_r = height[r]

            # - If left_height < right_height, then right side definitely has a higher max
            # - So we can safely process the left side
            # - Vice versa for the right side

            # We're not splitting the problem - we're choosing which side we can safely process
            # based on which side gives us enough information to make a definitive calculation.

            # The algorithm is brilliant because it realizes:
            # We don't need to know the exact maximum on both sides -
            # we just need to know which side is the limiting factor!

            # Think of it like this:
            # If I'm standing between two walls, the water level is determined by the shorter wall
            # If I can see that the right wall is definitely taller than where I'm standing, then I only need to worry about the left wall height
            # I don't need to measure the exact height of the right wall!

            if curr_height_l < curr_height_r:
                # Process left side
                if curr_height_l >= max_height_l:
                    max_height_l = curr_height_l
                else:
                    water_trapped += max_height_l - curr_height_l
                l += 1

            else:
                # Process right side
                if curr_height_r >= max_height_r:
                    max_height_r = curr_height_r
                else:
                    water_trapped += max_height_r - curr_height_r
                r -= 1

        return water_trapped

        #     Complexity Analysis
        # Time Complexity: O(n) - single pass through the array
        # Space Complexity: O(1) - only using variables, no extra arrays

        # ! sol2: brute force
        # For each position, find max height to left and right,
        # then calculate water that can be trapped.
        if not height:
            return 0

        water_trapped = 0
        n = len(height)

        for i in range(1, n - 1):
            left_max = 0
            for j in range(i):
                left_max = max(left_max, height[j])

            right_max = 0
            for j in range(i + 1, n):
                right_max = max(right_max, height[j])

            water_level = min(left_max, right_max)

            if water_level > height[i]:
                water_trapped += water_level - height[i]

        return water_trapped

        # Time Complexity: O(n²) - for each position, scan left and right
        # Space Complexity: O(1) - no extra space


# @lc code=end


#
# @lcpr case=start
# [0,1,0,2,1,0,1,3,2,1,2,1]\n
# @lcpr case=end

# @lcpr case=start
# [4,2,0,3,2,5]\n
# @lcpr case=end

#
