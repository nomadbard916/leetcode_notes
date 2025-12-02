#
# @lc app=leetcode id=41 lang=python3
# @lcpr version=30201
#
# [41] First Missing Positive
#

# @lc code=start
from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # KWs
        """
        - noun: array, (positive) integers
        - verb: find

        """

        # pattern
        """
        # thought of binary mask immediately
        - find missing positive -> search for gap
        - smallest positive integer -> minimum finding
        - not present in array -> presence check
        """

        # constraints
        """
        unsorted -> no ordering
        integer array
        return smallest positive integer
        O(n) time -> linear ok, need to start from 1 sequentially
        O(1) aux space -> may be in-place modification, no extra dict
        first missing
        full positive integer space
        nums array length not important
        """

        # problem specific pattern keywords
        """
        - index as hash key: position i stores value i+1
        - cyclic sort pattern: place each number at its "correct position"
        - marking with negation: use sign to mark presence
        """

        # ! sol1: cyclic sort
        """
        Find the smallest missing positive integer using O(n) time and O(1) space.

        Approach: Use the array itself as a hash table by placing each number
        at its "correct" position (number k goes to index k-1).
        """
        n = len(nums)
        if n == 0:
            return 1

        # step 1: place each number in its correct position
        # number k should be at index k-1 (if k is in range [1,n])
        # for example: [3,4,-1,1] => [1,-1,3,4]; [1,10000,3] => [1,10000,3]
        # it's never creating new memory space
        # enumerate(nums) cannot be used here as it's bounded to the original arrangement
        # and won't update in the process
        for i in range(n):
            curr_num = nums[i]
            # keep swapping until current position has correct value or value is out of range
            # Why the while loop doesn't cause O(n²):
            # Each element is moved at most once to its target position
            # Once placed correctly, it's never moved again
            # Total swaps ≤ n
            while 1 <= curr_num <= n and nums[curr_num - 1] != curr_num:
                # swap nums[i] to its correct position
                correct_idx = curr_num - 1
                nums[i], nums[correct_idx] = nums[correct_idx], curr_num
                # refresh after it's updated
                curr_num = nums[i]

        # step 2: find the first position where numbers doesn't match
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        return n + 1

        # ! sol2: just sort, it should actually go first in interview
        nums.sort()
        expected_missing = 1
        for num in nums:
            if num == expected_missing:
                expected_missing += 1
            elif num > expected_missing:
                return expected_missing
        return expected_missing

        """
        | Approach | Time | Space | Meets Constraints? |
        |----------|------|-------|-------------------|
        | Sorting | O(n log n) | O(1) or O(n)* | ❌ Time too slow |
        | Hash Set | O(n) | O(n) | ❌ Space too much |
        | Cyclic Sort | O(n) | O(1) | ✅ Perfect! |
        """


# @lc code=end


#
# @lcpr case=start
# [1,2,0]\n
# @lcpr case=end

# @lcpr case=start
# [3,4,-1,1]\n
# @lcpr case=end

# @lcpr case=start
# [7,8,9,11,12]\n
# @lcpr case=end

#
