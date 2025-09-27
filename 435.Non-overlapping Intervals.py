#
# @lc app=leetcode id=435 lang=python3
# @lcpr version=30201
#
# [435] Non-overlapping Intervals
#

# @lc code=start
from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        intervals.sort(key=lambda x: x[1])

        removed_count = 0

        last_end = intervals[0][1]

        for i in range(1, len(intervals)):
            start, end = intervals[i]

            if start < last_end:
                removed_count += 1
            else:
                last_end = end

        return removed_count


# @lc code=end


#
# @lcpr case=start
# [[1,2],[2,3],[3,4],[1,3]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,2],[1,2],[1,2]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,2],[2,3]]\n
# @lcpr case=end

#
