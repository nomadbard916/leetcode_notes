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
        # Key Insight - Greedy Strategy:
        # The optimal approach is to always keep the interval with the earliest end time when there's an overlap.
        # Why? Because keeping an interval that ends earlier leaves more room for future intervals,
        # maximizing our chances of keeping more intervals overall.

        # Why this works:
        # By always choosing intervals that end earliest, we maximize the remaining time space
        # This greedy choice leads to the globally optimal solution
        # It's similar to the classic "Activity Selection Problem"

        # Alternative sorting strategies:
        # - Sorting by start time doesn't work optimally
        # - Sorting by interval length doesn't work either
        # - Only sorting by end time guarantees optimal solution
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

        # Time and Space Complexity
        # Time Complexity: O(n log n) - dominated by the sorting step
        # Space Complexity: O(1) - only using constant extra space (not counting input)


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
