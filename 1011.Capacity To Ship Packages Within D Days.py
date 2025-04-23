#
# @lc app=leetcode id=1011 lang=python3
# @lcpr version=30104
#
# [1011] Capacity To Ship Packages Within D Days
#

# @lc code=start
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)  # minimum possible capacity
        right = sum(weights)  # maximum possible capacity

        def can_ship_in_days(capacity: int) -> int:
            current_days = 1
            current_load = 0

            for weight in weights:
                if current_load + weight > capacity:
                    current_days += 1
                    current_load = weight
                else:
                    current_load += weight
            return current_days

        # Binary search for minimum capacity
        while left < right:
            mid = (left + right) // 2
            if (can_ship_in_days(mid)) <= days:
                right = mid
            else:
                left = mid + 1

        return left


# @lc code=end


#
# @lcpr case=start
# [1,2,3,4,5,6,7,8,9,10]\n5\n
# @lcpr case=end

# @lcpr case=start
# [3,2,2,4,1,4]\n3\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,1,1]\n4\n
# @lcpr case=end

#
