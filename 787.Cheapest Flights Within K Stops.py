#
# @lc app=leetcode id=787 lang=python3
# @lcpr version=30201
#
# [787] Cheapest Flights Within K Stops
#

# @lc code=start
from collections import defaultdict, deque
from typing import List, Union


class Solution:
    def findCheapestPrice(
        self, n: int, flights: List[List[int]], src: int, dst: int, k: int
    ) -> int:
        # keyword
        """
        * nouns:
        n city
        connected
        some number of
        flight[]: [from, to, price] (weight)
        src
        dst
        k

        * verbs:
        "find" cheapest path
        "minimize" cost
        "travel" via flights
        """

        # pattern
        """
        "cheapest" → optimization problem; how do we track cost?
        "flights within K stops" → constrained path finding
        "at most K stops" → limited intermediate nodes
        graph with weighted weights -> shortest path variant, DFS & BFS (maybe, as it's optimization)
        dijkstra? (go-to, but hard to write)

        adjency list?

        => shortest path with constraints
        """

        # constraint
        """
        n cities (up to 100, small)
        flights (directed edges): up to n * (n-1)
        prices 1~10000
        k stops 0~n-1
        * key constraint: limited number of intermediate stops, not just shortest path

        cheapest price => min cost (tricky as we might take longer paths if cheaper)

        src to dst => connectivity with weights, path finding
        at most k stops => optimization, bounded search (tricky, may be some kind of sorting)
        don't need to worry about cycle as prices are positive
        """

        # mental category
        """
        graph traversal with weight (BFS with state tracking/Dijkstra)
        optimization, min cost

        Category: Shortest path with constraints
        Sub-category: Limited-depth shortest path
        NOT standard Dijkstra (which finds absolute shortest) because we have stop limit
        """

        # problem specific pattern keywords
        """
        state tracking: city, cost
        BFS with state tracking
        """
        # * Dijkstra can be thought of immediately with weighted graph, but let's try BFS first...
        # ! sol1: BFS with state tracking

        # build adjacency list
        graph = defaultdict(list)
        for from_city, to_city, price in flights:
            graph[from_city].append((to_city, price))

        # track min cost to reach each city
        # we update this as we find cheaper paths
        INF = float("inf")
        min_cost = [INF] * n
        min_cost[src] = 0

        # BFS queue: (current_city, cost_so_far)
        queue = deque([(src, 0)])
        stops = 0

        # process level by level (each level = one stop  )
        while queue and stops <= k:
            # process all cities at current level
            size = len(queue)
            for _ in range(size):
                current_city, current_cost = queue.popleft()

                # exploring all neighbor
                for next_city, price in graph[current_city]:
                    new_cost = current_cost + price

                    # only continue if we found a cheapter path
                    # this pruning is crucial for efficiency
                    if new_cost < min_cost[next_city]:
                        min_cost[next_city] = new_cost
                        queue.append((next_city, new_cost))

            stops += 1

        if min_cost[dst] != INF:
            return min_cost[dst]  # type: ignore

        return -1

        # Time Complexity: O(k × E) where E is number of flights
        # - We process at most k+1 levels
        # - Each flight can be explored multiple times (once per level)

        # Space Complexity: O(n) for the queue and min_cost array


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
