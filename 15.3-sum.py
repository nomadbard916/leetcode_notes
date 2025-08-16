#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Edge case
        LEN = len(nums)
        if LEN < 3:
            return []

        # Sort first to help with duplicate handling
        nums.sort()
        unique_triplets: set[tuple] = (
            set()
        )  # Use set to automatically handle duplicates

        # Fix the first element of triplet,
        # so it needs leave two places for second and third elements
        # enumerate cannot be used as it's args is about "start"
        for first_idx in range(LEN - 2):
            # Skip duplicates for first element
            first_element = nums[first_idx]
            if first_idx > 0 and first_element == nums[first_idx - 1]:
                continue

            seen_elements: set[int] = (
                set()
            )  # Track elements we've seen for current first_element

            # Look for second and third elements in remaining array
            for second_element in nums[first_idx + 1 :]:
                # Calculate what the third element should be; it's essentially complement
                third_element = -(first_element + second_element)

                # Check if we've seen the third element before
                if third_element in seen_elements:
                    # Found a valid triplet! Add to result
                    triplet = tuple(
                        sorted([first_element, second_element, third_element])
                    )
                    unique_triplets.add(triplet)

                # Add current element to seen set for future iterations
                seen_elements.add(second_element)

        # Convert set of tuples back to list of lists
        return [list(triplet) for triplet in unique_triplets]

        # sol 2: explicit two pointers.
        # sol 1 follows the thinking path of 2-sum
        # class Solution(object):
        #     def threeSum(self, nums):
        #         """
        #         :type nums: List[int]
        #         :rtype: List[List[int]]
        #         """
        #         # edge case
        #         if len(nums) < 3:
        #             return []
        #         res = []
        #         nums.sort()
        #         for i in range(len(nums)):
        #             # skip duplicate elements
        #             if i > 0 and nums[i] == nums[i - 1]:
        #                 continue
        #             l, r = i + 1, len(nums) - 1
        #             while l < r:
        #                 s = nums[i] + nums[l] + nums[r]
        #                 if s < 0:
        #                     # move l to the right
        #                     l += 1
        #                 elif s > 0:
        #                     # move r to the left
        #                     r -= 1
        #                 else:
        #                     res.append([nums[i], nums[l], nums[r]])
        #                     # skip duplicate elements
        #                     while l < r and nums[l] == nums[l + 1]:
        #                         l += 1
        #                     while l < r and nums[r] == nums[r - 1]:
        #                         r -= 1
        #                     l += 1
        #                     r -= 1

        #         return res


# @lc code=end
