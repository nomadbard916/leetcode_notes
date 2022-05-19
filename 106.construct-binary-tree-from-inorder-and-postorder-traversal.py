#
# @lc app=leetcode id=106 lang=python3
#
# [106] Construct Binary Tree from Inorder and Postorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=Optional[TreeNode], right=Optional[TreeNode]):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder or not postorder:
            return

        root_val = postorder.pop()
        root = TreeNode(root_val)
        index = inorder.index(root_val)

        root.right = self.buildTree(inorder[index + 1 :], postorder)
        root.left = self.buildTree(inorder[:index], postorder)

        return root


# @lc code=end
