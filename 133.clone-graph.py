#
# @lc app=leetcode id=133 lang=python3
#
# [133] Clone Graph
#

# @lc code=start

# c.f.: 138

# Definition for a Node.
from typing import Dict, Optional


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    # key challenges are:
    # - Handling cycles - graphs can have circular references, so we need to track visited nodes
    # - Deep copying - creating new nodes rather than copying references
    # - Preserving relationships - ensuring all neighbor connections are maintained

    def cloneGraph(self, node: Node) -> Optional[Node]:
        # or we can put it in dfs() args to save space, but less intuitive
        cloned: Dict[Node, Node] = {}

        # The DFS approach with a HashMap is most commonly used because:
        # - It naturally handles the recursive structure of graphs
        # - The HashMap prevents infinite recursion by tracking already-cloned nodes
        # - It's intuitive and has optimal time/space complexity
        def dfs(node: Node) -> Optional[Node]:
            if not node:
                return
            if node in cloned:
                return cloned[node]

            # create clone of current node
            node_clone = Node(node.val)
            cloned[node] = node_clone

            # filling in neighbors for each node clone
            for neighbor in node.neighbors:
                neighbor_clone = dfs(neighbor)
                if neighbor_clone:
                    node_clone.neighbors.append(neighbor_clone)

            return node_clone

        return dfs(node)

        # Complexity Analysis
        # - Time Complexity: O(N + M)
        # N = number of nodes
        # M = number of edges
        # We visit each node and edge exactly once

        # - Space Complexity: O(N)
        # HashMap to store N cloned nodes
        # Recursion stack depth up to N (in worst case of linear graph)


# @lc code=end
