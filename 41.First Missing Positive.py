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

        mask = [0] * (2**31 - 1)
        for num in nums:
            if num > 0:
                compensate_i = num - 1
                mask[compensate_i] = 1
        for i, bin_val in enumerate(mask):
            if bin_val == 0:
                return i + 1

        return 1
        # ! sol2: binary mask, buts uses O(n) space complexity


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
