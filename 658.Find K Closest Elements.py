#
# @lc app=leetcode id=658 lang=python3
# @lcpr version=30104
#
# [658] Find K Closest Elements
#

# @lc code=start
from typing import List


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        def left_bound_binary_search(nums: List[int], target: int):
            left = 0
            right = len(nums)
            while left < right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    right = mid
                elif nums[mid] < target:
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid
            return left

        # * two pointers from center
        res = []
        p = left_bound_binary_search(arr, x)
        # range: (left, right)
        left, right = p - 1, p
        # expand until there are k elements included
        while right - left - 1 < k:
            if left == -1:
                right += 1
            elif right == len(arr):
                left -= 1
            elif x - arr[left] > arr[right] - x:
                right += 1
            else:
                left -= 1
        for i in range(left + 1, right):
            res.append(arr[i])
        return res


# @lc code=end


#
# @lcpr case=start
# [1,2,3,4,5]\n4\n3\n
# @lcpr case=end

# @lcpr case=start
# [1,1,2,3,4,5]\n4\n-1\n
# @lcpr case=end

#
