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
        if len(nums) < 3:
            return []

        # Sort first to help with duplicate handling
        nums.sort()
        unique_triplets = set()  # Use set to automatically handle duplicates

        # Fix the first element of triplet
        for first_idx in range(len(nums) - 2):
            # Skip duplicates for first element
            if first_idx > 0 and nums[first_idx] == nums[first_idx - 1]:
                continue

            first_element = nums[first_idx]
            seen_elements = set()  # Track elements we've seen for current first_element

            # Look for second and third elements in remaining array
            for second_element in nums[first_idx + 1 :]:
                # Calculate what the third element should be
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
