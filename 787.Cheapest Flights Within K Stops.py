#
# @lc app=leetcode id=787 lang=python3
# @lcpr version=30201
#
# [787] Cheapest Flights Within K Stops
#

# @lc code=start
from typing import List


class Solution:
    def findCheapestPrice(
        self, n: int, flights: List[List[int]], src: int, dst: int, k: int
    ) -> int:
        # keyword
        """
        n city
        connected
        some number of
        flight[]: [from, to, price]
        src
        dst
        k
        """

        # pattern
        """
        graph -> DFS & BFS (maybe, as it's optimization)
        dijkstra?

        adjency list?
        """
        # constraint
        """
        cheapest price => optimization
        src to dst => connectivity
        at most k => optimization
        """

        return -1


# @lc code=end


#
# @lcpr case=start
# 4\n[[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]]\n0\n3\n1\n
# @lcpr case=end

# @lcpr case=start
# 3\n[[0,1,100],[1,2,100],[0,2,500]]\n0\n2\n1\n
# @lcpr case=end

# @lcpr case=start
# 3\n[[0,1,100],[1,2,100],[0,2,500]]\n0\n2\n0\n
# @lcpr case=end

#
