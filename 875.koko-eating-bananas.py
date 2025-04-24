#
# @lc app=leetcode id=875 lang=python3
#
# [875] Koko Eating Bananas
#

# @lc code=start
import math
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # actually two pointer with upper and lower limits, or l and r
        # any speed greater than max(piles) is meaningless as it still count as 1h

        # it's still guessing, but we can use binary search to cut half the guess

        min_speed, max_speed = 1, max(piles)

        while min_speed <= max_speed:
            mid_speed = (min_speed + max_speed) // 2
            curr_total_h = 0

            for pile in piles:
                curr_total_h += math.ceil(pile / mid_speed)
            # bisect right
            if curr_total_h <= h:
                # mid speed works, so let's search lower
                max_speed = mid_speed - 1
            else:
                # too slow, need to accelerate by searching higher
                min_speed = mid_speed + 1

        # loop ends with min_speed > max_speed
        # min_speed will be the first speed that works
        # max_speed will be the largest speed that's too slow

        return min_speed


# @lc code=end
