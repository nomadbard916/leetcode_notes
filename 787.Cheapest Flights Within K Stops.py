#
# @lc app=leetcode id=787 lang=python3
# @lcpr version=30201
#
# [787] Cheapest Flights Within K Stops
#

# @lc code=start
from collections import defaultdict, deque
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
        flight[]: [from, to, price] (weight)
        src
        dst
        k

        "find" cheapest path
        "travel" via flights
        "stop" up to k times
        """

        # pattern
        """
        graph -> DFS & BFS (maybe, as it's optimization)
        dijkstra? (go-to, but hard to write)

        adjency list?

        => shortest path with constraints
        """
        # constraint
        """
        n cities (up to 100, small)

        cheapest price => min cost (tricky as we might take longer paths if cheaper)
        src to dst => connectivity with weights, path finding
        at most k stops => optimization, bounded search (tricky, may be some kind of sorting)
        don't need to worry about cycle as prices are positive
        """

        # mental category
        """
        graph traversal (BFS/Dijkstra)
        optimization, min cost
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
