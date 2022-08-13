#
# @lc app=leetcode id=133 lang=python3
#
# [133] Clone Graph
#

# @lc code=start

# c.f.: 138

# Definition for a Node.
from typing import Optional


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    visited: dict = {}

    def cloneGraph(self, node: Node) -> Optional[Node]:
        return self.dfs(node)

    def dfs(self, node: Node) -> Optional[Node]:
        if not node:
            return
        if node in self.visited:
            return self.visited[node]

        # clone the node with only value and empty neighbors
        node_clone = Node(node.val, [])

        # record the current node, which will be manipulated by reference later
        self.visited[node] = node_clone

        # filling in neighbors for each node clone
        for neighbor in node.neighbors:
            # reaching the end first by dfs, then leveling up
            neighbor_clone = self.dfs(neighbor)
            if neighbor_clone:
                node_clone.neighbors.append(neighbor_clone)

        return node_clone


# @lc code=end
