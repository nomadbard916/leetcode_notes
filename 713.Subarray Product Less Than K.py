#
# @lc app=leetcode id=713 lang=python3
# @lcpr version=30104
#
# [713] Subarray Product Less Than K
#

# @lc code=start
from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        # ! sliding window, maybe compare with prefix sum?
        # using "prefix product" overcomplicates the solution ith O (n log n),
        # as it asks for "less than", not an exact value.
        # plus, sliding window resets the product when encountering zero

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

        # ref only: prefix product, should combine binary search
        # problems in this way:
        # 1. not asking a fixed value, sliding window is better at that
        # 2. if array contains zero, division by zero will cause trouble;
        # while sliding window fixes this automatically
        if k <= 1:
            return 0

        n = len(nums)
        # Create prefix product array
        prefix = [1] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] * nums[i]

        count = 0
        # For each starting position
        for i in range(n):
            left, right = i, n
            # Binary search to find the longest subarray starting at i with product < k
            while left < right:
                mid = (left + right) // 2
                # Calculate product from i to mid
                if i == 0:
                    current_product = prefix[mid + 1]
                else:
                    current_product = prefix[mid + 1] / prefix[i]

                if current_product < k:
                    left = mid + 1
                else:
                    right = mid

            # left - i represents the number of valid subarrays starting at position i
            count += left - i

        return count

        # time complexity: O(n log n) due to binary search


# @lc code=end


#
# @lcpr case=start
# [10,5,2,6]\n100\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3]\n0\n
# @lcpr case=end

#
