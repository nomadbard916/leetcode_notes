#
# @lc app=leetcode id=16 lang=python3
# @lcpr version=30201
#
# [16] 3Sum Closest
#

# @lc code=start
from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        closest_sum = float("inf")

        # fix the first element and use two pointers for the remaining two
        for i in range(n - 2):  # Leave space for at least 2 more elements
            left = i + 1
            right = n - 1

            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]

                if current_sum == target:
                    return current_sum

                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum

                if current_sum < target:
                    # need larger sum
                    left += 1
                else:
                    # need smaller sum
                    right -= 1

        return int(closest_sum)

        # Time Complexity: O(n²)
        # Sorting: O(n log n)
        # Nested loops: O(n) × O(n) = O(n²)
        # Overall: O(n²) dominates

        # Space Complexity: O(1)
        # Only using a constant amount of extra space
        # The sorting is typically done in-place


# @lc code=end


#
# @lcpr case=start
# [-1,2,1,-4]\n1\n
# @lcpr case=end

# @lcpr case=start
# [0,0,0]\n1\n
# @lcpr case=end

#
