#
# @lc app=leetcode id=543 lang=python3
#
# [543] Diameter of Binary Tree
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
    diameter = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # essentially find the max sum of the depth in left and right child tree
        # cf. 104, 110, 124

        # Key Insights:
        # - The diameter through any node equals the sum of the depths of its left and right subtrees
        # - We need to check every node as a potential "center" of the longest path
        # - We can solve this in one traversal by combining depth calculation with diameter tracking

        if not root:
            return 0

        self.max_depth(root)

        return self.diameter

    def max_depth(self, root: Optional[TreeNode]):
        """actually DFS post-order, so we may know the info about each subtree"""

        if not root:
            return 0

        left_depth = self.max_depth(root.left)
        right_depth = self.max_depth(root.right)

        # The diameter through this node is left_depth + right_depth
        # (the path goes down left subtree, through current node, down right subtree)
        curr_diameter = left_depth + right_depth
        self.diameter = max(self.diameter, curr_diameter)

        # after checking root exists,
        # the depth is at least 1 by linking root to current child
        return max(left_depth, right_depth) + 1

        #         Time & Space Complexity:

        # Time Complexity: O(n) - We visit each node exactly once
        # Space Complexity: O(h) - Where h is the height of the tree (recursion stack)

        # Best case (balanced): O(log n)
        # Worst case (skewed): O(n)


# @lc code=end
