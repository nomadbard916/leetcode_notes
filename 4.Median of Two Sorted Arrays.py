#
# @lc app=leetcode id=4 lang=python3
# @lcpr version=30201
#
# [4] Median of Two Sorted Arrays
#

# @lc code=start
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Thought Process Chain
        # - "O(log(m+n)) is suspicious" → This is logarithmic. What DS/algorithm does logarithmic?
        # Binary search, balanced trees, heaps...
        # - "But we need to find a position" → We need to find WHERE the median is without merging.
        # This smells like finding a threshold or boundary—classic binary search territory.
        # - "The constraint is the key" → The problem says "without merging."
        # If you can't see all elements, binary search is essentially your only tool for algorithmic speedup.
        # - "Think about what makes a median" → The median is about position, not values.
        # In a merged array, the median is at a specific index.
        # Even though we can't merge, can we figure out which elements would be at that position?
        # Yes—through strategic partitioning.

        # ensure nums1 is the smaller array to optimize binary search
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)

        left, right = 0, m

        while left <= right:
            # partition1 is the number of elements from nums1 on the left side
            partition1 = (left + right) // 2
            # partition2 is the number of elements from nums2 on the left side
            partition2 = (m + n + 1) // 2 - partition1

            # Handle edge cases where partition is at the boundary
            maxLeft1 = float("-inf") if partition1 == 0 else nums1[partition1 - 1]
            minRight1 = float("inf") if partition1 == m else nums1[partition1]

            maxLeft2 = float("-inf") if partition2 == 0 else nums2[partition2 - 1]
            minRight2 = float("inf") if partition2 == n else nums2[partition2]

            # Check if we found a valid partition
            if maxLeft1 <= minRight2 and maxLeft2 <= minRight1:
                # If total length is even
                if (m + n) % 2 == 0:
                    return (max(maxLeft1, maxLeft2) + min(minRight1, minRight2)) / 2
                else:
                    return float(max(maxLeft1, maxLeft2))
            # Move partition to the right if maxLeft1 is too large
            elif maxLeft1 > minRight2:
                right = partition1 - 1
                # Move partition to the left if maxLeft1 is too small
            else:
                left = partition1 + 1

        # Should never reach here with valid input
        return -1


# @lc code=end


#
# @lcpr case=start
# [1,3]\n[2]\n
# @lcpr case=end

# @lcpr case=start
# [1,2]\n[3,4]\n
# @lcpr case=end

#
