#
# @lc app=leetcode id=310 lang=python3
# @lcpr version=30104
#
# [310] Minimum Height Trees
#

# @lc code=start
from collections import defaultdict, deque
from typing import List


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # reverse BFS: start from all the leaf nodes then BFS upwards,
        # so the breadth of the tree can be as even as possible
        # the solution happens when the center has only 1 or 2 nodes (totally symmetric so both can be root)

        # Edge case: single node
        if n == 1:
            return [0]

        # * step 1: build adjacency list graph
        graph = defaultdict(set)
        for u, v in edges:
            # non-directional => see it as bi-directional
            graph[u].add(v)
            graph[v].add(u)

        # * step 2: find all the leaf nodes which have only one connection
        leaf_q = deque()
        for i in range(n):
            connection_degree = len(graph[i])
            if connection_degree == 1:
                leaf_q.append(i)

        # * step 3: keep deleting leaf nodes, until remaining <=2
        remaining_nodes_count = n
        while remaining_nodes_count > 2:
            leaf_count = len(leaf_q)
            remaining_nodes_count -= leaf_count
            for _ in range(leaf_count):
                cur_leaf_node = leaf_q.popleft()

                for neighbor in graph[cur_leaf_node]:
                    graph[neighbor].remove(cur_leaf_node)
                    # it's like "peeling":
                    # when the outermost leaf is removed,
                    # the one-layer-inner one may become the new leaf,
                    # when it has only one connection, then added into queue
                    connection_degree = len(graph[neighbor])
                    if connection_degree == 1:
                        leaf_q.append(neighbor)
        # * step 4: the remaining one or two nodes are the root
        return list(leaf_q)


# @lc code=end


#
# @lcpr case=start
# 4\n[[1,0],[1,2],[1,3]]\n
# @lcpr case=end

# @lcpr case=start
# 6\n[[3,0],[3,1],[3,2],[3,4],[5,4]]\n
# @lcpr case=end

#
