#
# @lc app=leetcode id=724 lang=python3
# @lcpr version=30104
#
# [724] Find Pivot Index
#

# @lc code=start
from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # it IS prefix sum, but we may not use it totally, instead maybe implicitly for simplicity
        # However, the explicit prefix sum approach has its own advantages:
        # - It separates the concerns of calculating prefix sums and finding the pivot
        # - The prefix sum array could be reused for other calculations if needed
        # - In some problems, having the full prefix sum array is necessary

        # sol1: implicit prefix sum
        total_sum = sum(nums)

        left_sum = 0

        for i, num in enumerate(nums):
            right_sum = total_sum - num - left_sum

            if left_sum == right_sum:
                return i

            left_sum += num

        return -1

        # time complexity: O(n)
        # space complexity: O(1)

        # sol2: prefix sum
        prefix_sums = [0]
        for num in nums:
            prefix_sums.append(prefix_sums[-1] + num)

        total_sum = prefix_sums[-1]

        for i in range(len(nums)):
            left_sum = prefix_sums[i]
            right_sum = total_sum - prefix_sums[i] - nums[i]

            if left_sum == right_sum:
                return i

        return -1

        # time complexity: O(n)
        # space complexity: O(n)


# @lc code=end


#
# @lcpr case=start
# [1,7,3,6,5,6]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3]\n
# @lcpr case=end

# @lcpr case=start
# [2,1,-1]\n
# @lcpr case=end

#
