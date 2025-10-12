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

        # in my own words:
        # Planning to divide two arrays in middle by smaller part and bigger part,
        # so the median will be the avg for the biggest in smaller and smallest in bigger.
        # ✓ Partition the first array to find the proper position for median
        # ✓ Plan to use binary search, so swap arrays to search on the smaller array for no-cost efficiency
        # ✓ The partition position of the second array is determined by the partition of array 1
        # ✓ Check boundary values i.e. min/max of left and right parts
        # We're checking TWO conditions simultaneously:
        # 1. maxLeft1 ≤ minRight2?
        # 2. maxLeft2 ≤ minRight1?

        # If BOTH are true → Found it! ✓
        # If maxLeft1 > minRight2 → partition1 is TOO FAR RIGHT
        #                         → Move right pointer LEFT
        # If maxLeft2 > minRight1 → partition1 is TOO FAR LEFT
        #                         → Move left pointer RIGHT
        # ✓ If not correct, move pointers until the answer is found

        # * step 1: ensure nums1 is the smaller array, to optimize binary search on smaller one
        # it's handy and does not cost much, so please do.
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)

        # * step2: Binary search on the smaller array to get the correct partition position
        left, right = 0, m

        while left <= right:
            # the variable name "count" for arrays was "partition", but that's confusing in concept.

            # For a valid partition:
            # - All elements on the left ≤ all elements on the right
            # - max(left) and min(right) give us the median for even-length arrays

            # partition1 is the number of elements from nums1 on the left side
            left_count_1 = (left + right) // 2
            # partition2 is the number of elements from nums2 on the left side, and it's influenced by partition 1.
            # The formula (m + n + 1) // 2 ensures the left side has enough elements:
            # -If total is even (e.g., 8 elements): left side needs 4 elements
            # - If total is odd (e.g., 9 elements): left side needs 5 elements (one more)
            left_count_2 = (m + n + 1) // 2 - left_count_1

            # * Step 3: Check validity, for each partition we check maxLeft1 < minRight2, and maxLeft2 < minRight1
            # If both conditions hold, we found the answer!
            # Handle edge cases where partition is at the boundary
            max_left_1 = float("-inf") if left_count_1 == 0 else nums1[left_count_1 - 1]
            min_right_1 = float("inf") if left_count_1 == m else nums1[left_count_1]

            max_left_2 = float("-inf") if left_count_2 == 0 else nums2[left_count_2 - 1]
            min_right_2 = float("inf") if left_count_2 == n else nums2[left_count_2]

            # * Step 4: Calculate median
            # Check if we found a valid partition
            if max_left_1 <= min_right_2 and max_left_2 <= min_right_1:
                # If total length is even
                if (m + n) % 2 == 0:
                    return (
                        max(max_left_1, max_left_2) + min(min_right_1, min_right_2)
                    ) / 2
                else:
                    return float(max(max_left_1, max_left_2))
            # Move partition to the right if maxLeft1 is too large
            elif max_left_1 > min_right_2:
                right = left_count_1 - 1
            # Move partition to the left if maxLeft1 is too small
            else:
                left = left_count_1 + 1

        # Should never reach here with valid input
        return -1

        # Time Complexity: O(log(min(m, n)))
        # Binary search runs on the smaller array, so it takes log(m) where m is the size of the smaller array
        # Each iteration does constant-time operations

        # Space Complexity: O(1)
        # We only use a few variables regardless of input size
        # No additional data structures are created


# @lc code=end


#
# @lcpr case=start
# [1,3]\n[2]\n
# @lcpr case=end

# @lcpr case=start
# [1,2]\n[3,4]\n
# @lcpr case=end

#
