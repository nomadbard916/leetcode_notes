#
# @lc app=leetcode id=99 lang=python3
#
# [99] Recover Binary Search Tree
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
    def inorder(self, root, list_nums, list_root):
        if not root:
            return

        self.inorder(root.left, list_nums, list_root)
        list_nums.append(root.val)
        list_root.append(root)
        self.inorder(root.right, list_nums, list_root)

    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        list_nums = []
        list_root = []

        # inorder traversal to visit nodes 'in order',
        # then record visited node's key-value pair and do sorting to be BST
        self.inorder(root, list_nums, list_root)
        list_nums.sort()

        # then visit the tree again to fill in correct value
        # on the same position with the same structure
        for i, current_root in enumerate(list_root):
            current_root.val = list_nums[i]


# @lc code=end

