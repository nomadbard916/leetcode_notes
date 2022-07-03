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
    def cloneGraph(self, node: Node) -> Node:
        return self.dfs(node, {})

    def dfs(self, node, visited) -> Optional[Node]:
        if not node:
            return
        if node in visited:
            return visited[node]

        node_clone = Node(node.val, [])
        visited[node] = node_clone

        for neighbor in node.neighbors:
            neighbor_copy = self.dfs(neighbor, visited)
            if neighbor_copy:
                node_clone.neighbors.append(neighbor_copy)

        return node_clone


# @lc code=end
