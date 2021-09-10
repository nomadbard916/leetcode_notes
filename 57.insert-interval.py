#
# @lc app=leetcode id=57 lang=python3
#
# [57] Insert Interval
#

# @lc code=start
from typing import List


class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        # ref: merge interval

        n = len(intervals)
        # sanity check immediately
        if n == 0:
            return [newInterval]

        # rearrange intervals to:
        # left to newInterval with all elements smaller then newInterval,
        # overlapping,
        # right to newInterval with all elements greater than newInterval
        left, right = [], []
        ni_start, ni_end = newInterval  # unpack

        for interval in intervals:
            current_start, current_end = interval

            if ni_start > current_end:
                left.append(interval)
            elif ni_end < current_start:
                right.append(interval)
            else:
                ni_start = min(ni_start, current_start)
                ni_end = max(ni_end, current_end)

        # concat the intervals
        return left + [[ni_start, ni_end]] + right


# @lc code=end

