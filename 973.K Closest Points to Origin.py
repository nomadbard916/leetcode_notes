#
# @lc app=leetcode id=973 lang=python3
# @lcpr version=30201
#
# [973] K Closest Points to Origin
#

# @lc code=start
import heapq
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # ! sol1: basic min-heap
        # Approach: Use a min-heap based on distance squared (to avoid sqrt computation)
        heap = []

        for point in points:
            x, y = point[0], point[1]
            dist_squared = x * x + y * y
            heapq.heappush(heap, (dist_squared, point))

        res = []
        for _ in range(k):
            dist_squared, point = heapq.heappop(heap)
            res.append(point)

        return res

        # Time: O(n log n) where n = len(points)
        # Space: O(n) for the heap

        # ! sol2: max heap of size k (optimized)

        # ! sol3: quick select


# @lc code=end


#
# @lcpr case=start
# [[1,3],[-2,2]]\n1\n
# @lcpr case=end

# @lcpr case=start
# [[3,3],[5,-1],[-2,4]]\n2\n
# @lcpr case=end

#
