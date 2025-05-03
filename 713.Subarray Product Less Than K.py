#
# @lc app=leetcode id=713 lang=python3
# @lcpr version=30104
#
# [713] Subarray Product Less Than K
#

# @lc code=start
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        # ! sliding window, maybe compare with prefix sum?
        # sanity check first
        if k <= 1:
            return 0

        l = 0
        res = 0
        product = 1

        for r in range(len(nums)):
            product *= nums[r]

            if product >= k:
                while product >= k and l <= r:
                    product /= nums[l]
                    l += 1

            res += r - l + 1

        return res


# @lc code=end


#
# @lcpr case=start
# [10,5,2,6]\n100\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3]\n0\n
# @lcpr case=end

#
