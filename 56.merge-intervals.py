#
# @lc app=leetcode id=56 lang=python3
#
# [56] Merge Intervals
#

# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # append the first period, then check if the following ones can be combined with the previous one
        # combine or append new, then repeatedly check every one until the last

        # sanity check
        if not intervals:
            return []

        intervals.sort(key=lambda i: i[0])

        ans = []
        ans.append(intervals[0])

        for i, current_interval in enumerate(intervals):
            if i == 0:  # already processed initially
                continue

            prev_interval = ans[-1]

            if current_interval[0] <= prev_interval[1]:
                prev_interval[1] = max(prev_interval[1], current_interval[1])
            else:
                ans.append(current_interval)

        return ans


# @lc code=end

