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

        # verbs and nouns
        """
        - noun:
        permutation, next permutation, (backtracking)
        sorted container (???)
        - verb:
        """

        # pattern keywords
        """
        inplace -> swapping, recording place with dict?
        next permutation: next bigger number, or the smallest when already biggest
        """

        # structural keywords
        """
        nums.length: 1~100 -> small
        nums[i]: 0~100 -> small
        """


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
