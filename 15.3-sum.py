#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # ! sol1: implicit two pointer, easier to understand
        # like two-sum that uses helper dict

        # key challenges
        # - Finding triplets that sum to 0
        # - Avoiding duplicate triplets
        # - Doing this efficiently

        # Edge case
        LEN = len(nums)
        if LEN < 3:
            return []

        # it looks like "two-pointer" could be applied => sort first
        nums.sort()
        unique_triplets: set[tuple] = set()

        # Fix the first element of triplet.
        # For each fixed element, we need to find two other elements that sum to the negative of this first element.
        # It needs leave two places for second and third elements.
        # enumerate() cannot be used as it's args is about "start"
        for first_idx in range(LEN - 2):
            # Skip duplicates for first element
            first_element = nums[first_idx]
            pre_first_element = nums[first_idx - 1]
            if first_idx > 0 and first_element == pre_first_element:
                continue

            seen_elements: set[int] = set()

            for second_element in nums[first_idx + 1 :]:
                # Calculate what the third element should be;
                # it's essentially the complement to sum of first and second
                third_element = -(first_element + second_element)

                if third_element in seen_elements:
                    # list cannot be hashed by set.add(),
                    # that's why we are using tuple and keep type converting
                    triplet = tuple(
                        sorted([first_element, second_element, third_element])
                    )
                    unique_triplets.add(triplet)

                seen_elements.add(second_element)

        return [list(triplet) for triplet in unique_triplets]

        # Time Complexity: O(n²)
        # Space Complexity: O(n) for the hash set

        # Pros: Intuitive if you're familiar with 2Sum
        # Cons: Extra space needed, slightly more complex duplicate handling

        # ! sol 2: explicit two pointers, more efficient

        # edge case
        if len(nums) < 3:
            return []
        nums.sort()
        res = []

        # fix the first number, then use l and r for second and third
        for i in range(len(nums)):
            # skip duplicate elements
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1

            # We move pointers based on whether the current sum is too small or too large
            while l < r:
                curr_sum = nums[i] + nums[l] + nums[r]
                # the smaller l too small, make it bigger
                if curr_sum < 0:
                    l += 1
                # the larger r too large, make it smaller
                elif curr_sum > 0:
                    r -= 1
                # answer found, further process
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    # skip duplicate elements
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    l += 1
                    r -= 1

        return res

        # - Time Complexity: O(n²)
        # Sorting takes O(n log n)
        # The outer loop runs n times
        # For each iteration, the two-pointer approach takes O(n) time
        # Overall: O(n log n) + O(n²) = O(n²)
        # - Space Complexity: O(1) or O(log n)
        # If we don't count the output array, we only use constant extra space
        # The sorting algorithm might use O(log n) space for recursion stack
        # Output space is not counted in space complexity analysis

        # Pros: More space efficient, elegant, easier to handle duplicates
        # Cons: Requires understanding of two-pointer technique


# @lc code=end
