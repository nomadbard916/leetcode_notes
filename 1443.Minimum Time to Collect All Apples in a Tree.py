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
        # * Build adjacency list representation of the tree
        neighbor_graph = [[] for _ in range(n)]
        for u, v in edges:
            neighbor_graph[u].append(v)
            neighbor_graph[v].append(u)

        # * calculate minimum time needed for subtree rooted at 'node'.
        def dfs(node: int, parent: int) -> int:
            total_time = 0

            node_neighbors = neighbor_graph[node]
            for neighbor in node_neighbors:
                # Going back to parent should be excluded from options,
                # to prevent infinite loops in DFS traversal.
                if neighbor == parent:
                    continue

                neighbor_time = dfs(neighbor, node)

                # * post order logic
                # If child subtree has apples:
                # The neighbor itself has an apple, OR the neighbor's subtree contains apples somewhere,
                # we need to visit it.
                # modifying total_time after post order traversal is totally fine
                # as it's a side effect of post order traversal.
                if neighbor_time > 0 or hasApple[neighbor]:
                    # This costs 2 time units (go there and come back)
                    # Visiting a neighbor costs neighbor_time + 2
                    # neighbor_time: Time to collect apples in neighbor's subtree
                    # +2: Time to go to neighbor and come back
                    total_time += neighbor_time + 2

            # Return total time for this subtree
            return total_time

        # Start DFS from root (node 0) with no parent (-1)
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
