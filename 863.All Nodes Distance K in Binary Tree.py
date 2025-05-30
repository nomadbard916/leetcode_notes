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
        # BFS vs DFS Trade-offs
        # BFS: More intuitive for distance problems, but uses more space
        # DFS: More space-efficient, but logic can be more complex

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

        # ! sol2: DFS with distance tracking
        # How DFS Works:
        # - For each node, determine if the target is in its subtree
        # - If target found, calculate distances and collect appropriate nodes
        # - Handle three cases: target in left subtree, right subtree, or current node is target
        # Why This Works:
        # - The formula accounts for the "cost" of traveling up to the common ancestor and then down to the other subtree
        # - It ensures we only look for nodes that, when combined with the crossing distance, give us exactly k total steps from the target
        # The same logic applies symmetrically when the target is in the right subtree and we're looking in the left subtree.
        # This is why the DFS solution is more complex than BFS - it has to carefully track these distance relationships, while BFS naturally handles distances through level-by-level exploration.

        result = []

        def collect_nodes_at_distance(node, distance, result):
            if not node or distance < 0:
                return
            if distance == 0:
                result.append(node.val)
                return

            collect_nodes_at_distance(node.left, distance - 1, result)
            collect_nodes_at_distance(node.right, distance - 1, result)

        def find_distance_to_target(node):
            """
            Returns distance from current node to target.
            Returns -1 if target is not in this subtree.
            """
            if not node:
                return -1

            # # Found target, collect all nodes at distance k in its subtree
            if node == target:
                collect_nodes_at_distance(node, k, result)
                return 0

            # check left subtree
            left_dist = find_distance_to_target(node.left)
            if left_dist != -1:
                # # Target found in left subtree. Current node is at distance k from target
                if left_dist + 1 == k:
                    result.append(node.val)
                else:
                    # Look for nodes at distance k in right subtree
                    # Distance Calculation:
                    # 1 Target to left child: left_dist steps
                    # 2 Left child to current node: 1 step
                    # 3 Current node to right child: 1 step
                    # 4 Total from target to right child: left_dist + 1 + 1 = left_dist + 2
                    # The Logic:
                    # - If we want total distance of k from target to some node in right subtree
                    # - And we already "used up" left_dist + 2 steps to reach the right subtree root
                    # - Then we need k - (left_dist + 2) = k - left_dist - 2 more steps within the right subtree
                    remaining_distance = k - (left_dist + 2)
                    collect_nodes_at_distance(node.right, remaining_distance, result)
                return left_dist + 1

            # check right subtree
            right_dist = find_distance_to_target(node.right)
            if right_dist != -1:
                # Target found in right subtree. Current node is at distance k from target
                if right_dist + 1 == k:
                    result.append(node.val)
                else:
                    # Look for nodes at distance k in left subtree
                    remaining_distance = k - (right_dist + 2)
                    collect_nodes_at_distance(node.left, remaining_distance, result)
                return right_dist + 1

        find_distance_to_target(root)
        return result

        # Time Complexity: O(n)
        # Each node is visited at most twice

        # Space Complexity: O(h) where h is the height of the tree
        # Recursion stack depth
        # No additional data structures needed


# @lc code=end


#
# @lcpr case=start
# [3,5,1,6,2,0,8,null,null,7,4]\n5\n2\n
# @lcpr case=end

# @lcpr case=start
# [1]\n1\n3\n
# @lcpr case=end

#
