#
# @lc app=leetcode id=42 lang=python3
# @lcpr version=30201
#
# [42] Trapping Rain Water
#

# @lc code=start
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        # ! sol1: two pointer, also most efficient
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


# @lc code=end


#
# @lcpr case=start
# [0,1,0,2,1,0,1,3,2,1,2,1]\n
# @lcpr case=end

# @lcpr case=start
# [4,2,0,3,2,5]\n
# @lcpr case=end

#
