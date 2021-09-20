#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#

# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # iterate twice, first save 'product of left' then 'product of right',
        # then multiply each element from these two, with leftmost and rightmost being 1.
        # e.g.: for [1,2,3,4], 'product of left goes: [1,1,2,6]
        # 'product of right goes: [24,12,4,1], therefore answer goes [24,12,8,6]
        ans = []
        length = len(nums)

        # going from left to right
        prod = 1
        for i in range(length):
            ans.append(prod)
            prod *= nums[i]

        # going from right to left
        prod = 1
        for i in range(length - 1, -1, -1):
            ans[i] *= prod
            prod *= nums[i]

        return ans


# @lc code=end

