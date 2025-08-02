#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#

# @lc code=start
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # binary search, consider current asc or desc ordering

        # sanity check
        if not nums:
            return -1

        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid

            # Determine which side is properly sorted
            if nums[left] <= nums[mid]:  # Left side is sorted
                # Check if target is in the sorted left side
                if nums[left] <= target < nums[mid]:
                    right = mid - 1  # Search left side
                else:
                    left = mid + 1  # Search right side
            else:  # Right side is sorted
                # Check if target is in the sorted right side
                if nums[mid] < target <= nums[right]:
                    left = mid + 1  # Search right side
                else:
                    right = mid - 1  # Search left side
        return -1


# @lc code=end
