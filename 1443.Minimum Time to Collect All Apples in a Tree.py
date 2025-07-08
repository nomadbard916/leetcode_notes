#
# @lc app=leetcode id=1443 lang=python3
# @lcpr version=30201
#
# [1443] Minimum Time to Collect All Apples in a Tree
#

# @lc code=start
from typing import List


class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        # Build adjacency list representation of the tree
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def dfs(node: int, parent: int) -> int:
            total_time = 0

            # Explore all children
            for child in graph[node]:
                if child != parent:  # Avoid going back to parent
                    child_time = dfs(child, node)

                    # If child subtree has apples, we need to visit it
                    # This costs 2 time units (go there and come back)
                    if child_time or hasApple[child]:
                        total_time += child_time + 2

            # Return total time for this subtree
            return total_time

        # Start DFS from root (node 0) with no parent (-1)
        # We don't add 2 for the root since we start there
        return dfs(0, -1)


# @lc code=end


#
# @lcpr case=start
# 7\n[[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]]\n[false,false,true,false,true,true,false]\n
# @lcpr case=end

# @lcpr case=start
# 7\n[[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]]\n[false,false,true,false,false,true,false]\n
# @lcpr case=end

# @lcpr case=start
# 7\n[[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]]\n[false,false,false,false,false,false,false]\n
# @lcpr case=end

#
