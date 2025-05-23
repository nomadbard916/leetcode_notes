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

        depth_sum = left_depth + right_depth
        self.diameter = max(self.diameter, depth_sum)

        # after checking root exists,
        # the depth is at least 1 by linking root to current child
        return max(left_depth, right_depth) + 1


# @lc code=end
