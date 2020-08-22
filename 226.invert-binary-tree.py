#
# @lc app=leetcode id=226 lang=python3
#
# [226] Invert Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        # every right node should be left, left be right
        # use the original function as traversal function

        if root is None:
            return

        right_node = self.invertTree(root.right)
        left_node = self.invertTree(root.left)

        # post order as left and right child should be known first
        root.left, root.right = right_node, left_node

        return root


# @lc code=end

