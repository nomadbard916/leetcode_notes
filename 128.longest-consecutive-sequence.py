#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#

# @lc code=start
from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest_streak = 0

        # lookup with hashmap with O(1)
        # deduplicate with set, which is based on hashmap
        nums_set = set(nums)
        for num in nums_set:
            #  continue if it's not the beginning of sequence,
            # and therefore cannot be the longest consecutive
            if num - 1 in nums_set:
                continue

            current_num = num
            current_streak = 1

            while current_num + 1 in nums_set:
                current_num += 1
                current_streak += 1

            longest_streak = max(longest_streak, current_streak)

        return longest_streak


# @lc code=end
