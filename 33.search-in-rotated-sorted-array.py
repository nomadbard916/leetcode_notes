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

            m_to_r_ordered = nums[mid] < nums[right]
            if m_to_r_ordered:
                left, right = self.assign_m_to_r(nums, target, left, right, mid)
            else:  # l_to_m_ordered
                left, right = self.assign_l_to_m(nums, target, left, right, mid)
        return -1

        # sol 2: with built-in as range nums is relatively small
        # return nums.index(target)

    def assign_l_to_m(
        self, nums, target, left: int, right: int, mid
    ) -> tuple[int, int]:
        if target < nums[mid] and target >= nums[left]:
            right = mid - 1
        else:
            left = mid + 1
        return left, right

    def assign_m_to_r(
        self, nums, target, left: int, right: int, mid
    ) -> tuple[int, int]:
        if target > nums[mid] and target <= nums[right]:
            left = mid + 1
        else:
            right = mid - 1
        return left, right


# @lc code=end
