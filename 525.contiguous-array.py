#
# @lc app=leetcode id=525 lang=python3
#
# [525] Contiguous Array
#

# @lc code=start
from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        # if 0 is taken as -1 since there only two numbers,
        # then the appearance of 2nd same summation just means
        # an equal number of 0 and 1;
        # the distance between 2nd and 1nd summation could be the max contiguous length.
        # keep iterating and updating.
        current_sum = 0
        sum_index_map = {}
        ans = 0

        # initialize sum 0 or num at non-existing index -1
        sum_index_map[0] = -1

        for i, num in enumerate(nums):
            if num == 0:
                current_sum -= 1
            else:
                current_sum += 1

            if current_sum in sum_index_map:
                ans = max(ans, i - sum_index_map[current_sum])
            else:
                sum_index_map[current_sum] = i

        return ans


# @lc code=end
