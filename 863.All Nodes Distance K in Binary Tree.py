#
# @lc app=leetcode id=863 lang=python3
# @lcpr version=30201
#
# [863] All Nodes Distance K in Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        # ! sol1: BFS with parent mapping (recommended)
        # This pattern of "convert tree to graph" is common when you need bidirectional traversal in trees.
        # Other problems where this helps:
        # - Finding LCA (Lowest Common Ancestor)
        # - Tree diameter problems
        # - Shortest path between any two nodes
        if k == 0:
            return [target.val]

        # * build parent mapping for each node to create undirected graph representation
        #  by traversing the whole tree

        def build_parent_map(
            node: Optional[TreeNode],
            parent: Optional[TreeNode],
            curr_parent_map: dict[TreeNode, Optional[TreeNode]],
        ) -> dict[TreeNode, Optional[TreeNode]]:
            if not node:
                return curr_parent_map
            curr_parent_map[node] = parent
            build_parent_map(node.left, node, curr_parent_map)
            build_parent_map(node.right, node, curr_parent_map)
            return curr_parent_map

        parent_map = build_parent_map(root, None, {})

        # * BFS from target node
        # Why BFS Works: BFS naturally explores nodes level by level,
        # where each level represents one unit of distance from the source.
        q = deque([target])
        visited_set = {target}
        distance = 0

        while q and distance < k:
            q_size = len(q)
            distance += 1
            for _ in range(q_size):
                curr_node = q.popleft()
                # check all neighbors: left child, right child, parent
                neighbors = []
                if curr_node.left:
                    neighbors.append(curr_node.left)
                if curr_node.right:
                    neighbors.append(curr_node.right)
                if parent_map[curr_node]:
                    neighbors.append(parent_map[curr_node])

                for n in neighbors:
                    if n not in visited_set:
                        visited_set.add(n)
                        q.append(n)

        # * collect all nodes at distance k
        result = []
        while q:
            curr_val = q.popleft().val
            result.append(curr_val)

        return result

        # Time Complexity: O(n) where n is the number of nodes
        # Building parent map: O(n)
        # BFS traversal: O(n) in worst case

        # Space Complexity: O(n)
        # Parent map: O(n)
        # Queue for BFS: O(n) in worst case
        # Visited set: O(n)


# @lc code=end


#
# @lcpr case=start
# [3,5,1,6,2,0,8,null,null,7,4]\n5\n2\n
# @lcpr case=end

# @lcpr case=start
# [1]\n1\n3\n
# @lcpr case=end

#
