#
# @lc app=leetcode id=152 lang=python3
#
# [152] Maximum Product Subarray
#

# @lc code=start
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # ref. : https://leetcode-solution-leetcode-pp.gitbook.io/leetcode-solution/medium/152.maximum-product-subarray

        # contiguous => sliding window, O(n) while brute force O(n^2)
        # a very small negative value multiplies a smaller negative value can be very big
        n = len(nums)

        #  set initial dummy state of max, min and ans, which will be substituted immediately
        max_val = min_val = 1
        ans = float("-inf")

        # need to start from nums[0] and end at nums[n], whereas i-1 means 'current' index
        for i in range(1, n + 1):
            original_max = max_val

            # possibilities can be:
            # numbers in a row and a single number
            # a and b here are 'updated' and keep updating
            max_val = max(
                original_max * nums[i - 1], min_val * nums[i - 1], nums[i - 1]
            )
            min_val = min(
                original_max * nums[i - 1], min_val * nums[i - 1], nums[i - 1]
            )

            #  keep updating maximum and make it current answer for current iteration
            ans = max(ans, max_val)

        return ans


# @lc code=end

