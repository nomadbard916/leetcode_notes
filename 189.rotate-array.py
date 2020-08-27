#
# @lc app=leetcode id=189 lang=python3
#
# [189] Rotate Array
#

# @lc code=start
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # # sol 1: find the relationship between old and new position
        n = len(nums)
        a = [0] * n
        for i in range(n):
            a[(i + k) % n] = nums[i]

        nums[:] = a

        # sol 2
        # avoid exceeding
        # real_k = k % len(nums)
        # reversed_nums = list(reversed(nums))
        # l = reversed_nums[:real_k]
        # r = reversed_nums[real_k:]

        # nums[:] = list(reversed(l)) + list(reversed(r))


# @lc code=end

