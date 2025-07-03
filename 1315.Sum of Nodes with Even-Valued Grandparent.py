#
# @lc app=leetcode id=1315 lang=python3
# @lcpr version=30201
#
# [1315] Sum of Nodes with Even-Valued Grandparent
#

# @lc code=start
# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        # ! sol1: DFS
        non_existing_node_val = -1

        def dfs(node: Optional[TreeNode], parent_val: int, grandparent_val: int) -> int:
            if not node:
                return 0

            # initialize sum for current subtree
            current_sum = 0

            grandparent_exists = grandparent_val != non_existing_node_val
            grandparent_is_even = grandparent_val % 2 == 0
            if grandparent_exists and grandparent_is_even:
                current_sum += node.val

            # recursion to next levels, with two layers above nodes info passed down
            left_sum = dfs(node.left, node.val, parent_val)
            right_sum = dfs(node.right, node.val, parent_val)

            return current_sum + left_sum + right_sum

        return dfs(root, non_existing_node_val, non_existing_node_val)

        # ! sol2: BFS
        def bfs(root: TreeNode) -> int:
            total_sum = 0
            if not root:
                return total_sum

            from collections import deque

            # Queue stores tuples: (node, parent_val, grandparent_val)
            # start from outside of tree, node doesn't exist yet
            q = deque([(root, non_existing_node_val, non_existing_node_val)])

            while q:
                node, parent_val, grandparent_val = q.popleft()

                grandparent_exists = grandparent_val != non_existing_node_val
                grandparent_is_even = grandparent_val % 2 == 0
                if grandparent_exists and grandparent_is_even:
                    total_sum += node.val

                # Add children to queue with updated parent/grandparent values
                if root.left:
                    q.append((node.left, node.val, parent_val))
                if root.right:
                    q.append((node.right, node.val, parent_val))

            return total_sum

        return bfs(root)

        # Time and Space Complexity:
        # Time Complexity: O(n)
        # We visit each node exactly once
        # For each node, we do constant time operations (checking even value, arithmetic)
        # Where n is the number of nodes in the tree

        # Space Complexity: O(h)
        # For DFS: O(h) where h is the height of the tree (recursion stack)
        # For BFS: O(w) where w is the maximum width of the tree (queue size)
        # In the worst case (skewed tree), h = n, so O(n)
        # In the best case (balanced tree), h = log(n), so O(log n)


# @lc code=end


#
# @lcpr case=start
# [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]\n
# @lcpr case=end

# @lcpr case=start
# [1]\n
# @lcpr case=end

#
