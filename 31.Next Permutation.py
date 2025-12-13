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

        """
        Modifies nums in-place to be the next lexicographical permutation.

        Algorithm:
        1. Find the rightmost 'pivot' where nums[i] < nums[i+1]
        2. If no pivot exists, reverse entire array (it's the largest permutation)
        3. Find the smallest number in nums[i+1:] that's greater than nums[i]
        4. Swap nums[i] with that number
        5. Reverse nums[i+1:] to get the smallest arrangement
        """
        n = len(nums)

        # step 1: find the pivot point (rightmost i where nums[i] < nums[i+1])
        # we scan from right to left to find where the sequence stops being descdending
        pivot = -1
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                pivot = i
                break

        # step 2: if no pivot found, array is in descending order
        # this is the largest permutation, so wrap around the smallest
        if pivot == -1:
            nums.reverse()
            return

        # step 3: find the smallest number > nums[pivot] in the suffix
        # since nums[pivot+1:] is in descending order, we scan from right
        successor = -1
        for i in range(n - 1, pivot, -1):
            if nums[i] > nums[pivot]:
                successor = i
                break

        # step 4: swap pivot with its successor
        nums[pivot], nums[successor] = nums[successor], nums[pivot]

        # step 5: reverse the suffix to get the smallest arrangement
        # after swapping, nums[pivot+1:] is still in descending order
        # we need ascending order for the next smallest permutation
        l, r = pivot + 1, n - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

        # Complexity Analysis
        # Time Complexity: O(n)
        # - Finding pivot: O(n) worst case
        # - Finding successor: O(n) worst case
        # - Swapping: O(1)
        # - Reversing suffix: O(n) worst case
        # - Overall: O(n)

        # Space Complexity: O(1)
        # - Only using a few variables (pivot, successor, left, right)
        # - All operations are in-place
        # - No additional data structures needed


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
