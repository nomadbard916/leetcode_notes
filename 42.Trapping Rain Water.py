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
        # ! sol1: two pointer, also most efficient
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
        l_max, r_max = 0, 0
        water_trapped: int = 0

        while l < r:
            if height[l] < height[r]:
                if height[l] >= l_max:
                    l_max = height[l]
                else:
                    water_trapped += l_max - height[l]
                l += 1

            else:
                if height[r] >= r_max:
                    r_max = height[r]
                else:
                    water_trapped += r_max - height[r]
                r -= 1
        return water_trapped

        #     Complexity Analysis
        # Time Complexity: O(n) - single pass through the array
        # Space Complexity: O(1) - only using variables, no extra arrays


# @lc code=end


#
# @lcpr case=start
# [0,1,0,2,1,0,1,3,2,1,2,1]\n
# @lcpr case=end

# @lcpr case=start
# [4,2,0,3,2,5]\n
# @lcpr case=end

#
