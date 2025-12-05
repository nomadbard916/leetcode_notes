#
# @lc app=leetcode id=31 lang=python3
# @lcpr version=30201
#
# [31] Next Permutation
#

# @lc code=start
from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # first thought: just sort and return

        # two dict: one for val->idx, one for permutation -> next

        # => turns out to be pivot

        # verbs and nouns
        """
        - noun:
        permutation, next permutation, (backtracking)
        lexicographic order
        sorted container (???)
        - verb: rearrange, find, replace
        """

        # pattern keywords
        """
        inplace -> swapping with constant space, recording place with dict?
        next permutation: next bigger number, or the smallest when already biggest -> sequence ordering
        "lexicographically next" → dictionary order, comparison

        """

        # structural keywords
        """
        nums.length: 1~100 -> small
        nums[i]: 0~100 -> small
        O(n) time, O(1) extra space
        """

        # algo concept
        """
        next greater -> finding pivot
        lexicographically -> left to right significance
        smallest possible -> minimizing changes from right
        in-place -> two-pointer, swapping
        """

        # mental categories
        """
        array manipulation
        greedy
        two pointer
        reverse operations
        """

        # tricky keywords


# @lc code=end


#
# @lcpr case=start
# [1,2,3]\n
# @lcpr case=end

# @lcpr case=start
# [3,2,1]\n
# @lcpr case=end

# @lcpr case=start
# [1,1,5]\n
# @lcpr case=end

#
