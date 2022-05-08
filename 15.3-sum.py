#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        LEN = len(nums)
        if LEN < 3:
            return []

        # it looks like two-pointer could be applied => sort first
        nums.sort()

        # prevent duplicates
        ans = set()

        # implicit two pointer
        # fix v as left pointer, below x as right pointer,
        # then the third must be the complement of v+x

        # don't count in the first and the last
        for i, v in enumerate(nums[:-2]):
            # don't count in duplicates
            if i >= 1 and v == nums[i - 1]:
                continue

            complements = set()
            # fix v as left pointer,
            # just add 1 to make the starting of right pointer x,
            # and check for their complement
            for x in nums[i + 1 :]:
                complement = -(v + x)
                if x not in complements:
                    complements.add(complement)
                else:
                    # list cannot be hashed by set.add()
                    ans.add((v, complement, x))

        return list(ans)

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
