#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input array is sorted
#

# @lc code=start
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        LENGTH = len(numbers)
        # sanity check:
        if LENGTH == 0:
            return [-1, -1]
        if numbers[0] > target:
            return [-1, -1]

        l, r = 0, LENGTH - 1

        while l < r:
            current_sum = numbers[l] + numbers[r]

            if current_sum == target:
                return [l + 1, r + 1]
            elif current_sum < target:
                l += 1
            else:
                r -= 1

        return [-1, -1]


# @lc code=end

