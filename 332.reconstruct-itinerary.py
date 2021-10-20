#
# @lc app=leetcode id=332 lang=python3
#
# [332] Reconstruct Itinerary
#

# @lc code=start
from typing import List
from collections import defaultdict


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # as we are going through the end of every possible path MECE
        # => DFS post-order traversal
        graph = defaultdict(list)

        # list every possible destinations for a departure
        for frm, to in tickets:
            graph[frm].append(to)

        for frm, tos in graph.items():
            # reverse sort so smaller lexical order stop will be popped first
            tos.sort(reverse=True)

        ans = []
        self.dfs(graph, ans, "JFK")

        # as it's essentially post-order traversal, the ans need to be flipped
        return ans[::-1]

    def dfs(self, graph, ans, dep):
        arrivals = graph[dep]
        while arrivals:
            # pop smallest lexical stop as visited
            v = graph[dep].pop()
            self.dfs(graph, ans, v)

        # append to ans when reaching the end
        ans.append(dep)


# @lc code=end

