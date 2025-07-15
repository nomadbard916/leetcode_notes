#
# @lc app=leetcode id=623 lang=python3
# @lcpr version=30201
#
# [623] Add One Row to Tree
#

# @lc code=start
# Definition for a binary tree node.
from collections import deque
from typing import Optional

# ! it cannot be uncommented, or the whole code breaks
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def addOneRow(
        self, root: Optional[TreeNode], val: int, depth: int
    ) -> Optional[TreeNode]:
        # ! sol1: BFS as the mainly recommended
        # Special case: if depth is 1, we need to create a new root
        if depth == 1:
            new_root = TreeNode(val)
            new_root.left = root
            return new_root

        queue = deque([(root, 1)])  # (node, current_depth)

        while queue:
            node, current_depth = queue.popleft()

            # * If we're at the target depth - 1, can modify children
            if current_depth == depth - 1:
                # Save original children
                original_left = node.left
                original_right = node.right

                # Create new nodes with the given value
                node.left = TreeNode(val)
                node.right = TreeNode(val)

                # Connect original children to new nodes
                node.left.left = original_left
                node.right.right = original_right
            # * Continue BFS if we haven't reached target depth - 1
            else:
                if node.left:
                    queue.append((node.left, current_depth + 1))
                if node.right:
                    queue.append((node.right, current_depth + 1))

        return root

        # ! sol2: DFS
        if depth == 1:
            new_root = TreeNode(val)
            new_root.left = root
            return new_root

        def dfs(node: Optional[TreeNode], current_depth: int) -> None:
            if not node:
                return

            if current_depth == depth - 1:
                # Save original children
                original_left = node.left
                original_right = node.right

                # Create new nodes and connect them
                node.left = TreeNode(val)
                node.right = TreeNode(val)
                node.left.left = original_left
                node.right.right = original_right
            else:
                # Continue DFS
                dfs(node.left, current_depth + 1)
                dfs(node.right, current_depth + 1)

        dfs(root, 1)
        return root

        # Complexity Analysis
        # Time Complexity: O(n)
        # - In the worst case, we might need to visit all nodes in the tree (when depth is very large)
        # - Each node is visited at most once

        # Space Complexity: O(w)
        # - Where w is the maximum width of the tree (maximum number of nodes at any level)
        # - For BFS: queue can hold at most w nodes
        # - For DFS: recursive call stack can be at most h (height of tree) in the worst case


# @lc code=end


#
# @lcpr case=start
# [4,2,6,3,1,5]\n1\n2\n
# @lcpr case=end

# @lcpr case=start
# [4,2,null,3,1]\n1\n3\n
# @lcpr case=end

#
