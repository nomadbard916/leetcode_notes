#
# @lc app=leetcode id=310 lang=python3
# @lcpr version=30104
#
# [310] Minimum Height Trees
#

# @lc code=start
from collections import deque
from typing import List


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        # * step 1: build graph
        graph = [[] for _ in range(n)]
        for edge in edges:
            # non-directional => see it as bi-directional
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])

        # * step 2: find all the leaf nodes
        q = deque()
        for i in range(n):
            if len(graph[i]) == 1:
                q.append(i)

        # * step 3: keep deleting leaf nodes, until remaining <=2
        node_count = n
        while node_count > 2:
            q_size = len(q)
            node_count -= q_size
            for _ in range(q_size):
                cur_node = q.popleft()

                # find neighbors to the current leaf node
                for neighbor in graph[cur_node]:
                    graph[neighbor].remove(cur_node)
                    # after removal, if there's only one connection, it means the node becomes a leaf
                    if len(graph[neighbor]) == 1:
                        q.append(neighbor)
        # * step 4: the remaining one is the root
        return list(q)


# @lc code=end


#
# @lcpr case=start
# 4\n[[1,0],[1,2],[1,3]]\n
# @lcpr case=end

# @lcpr case=start
# 6\n[[3,0],[3,1],[3,2],[3,4],[5,4]]\n
# @lcpr case=end

#
