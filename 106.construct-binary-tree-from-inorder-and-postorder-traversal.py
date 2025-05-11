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
        # TODO: Q889 with framework from labuladong
        # https://labuladong.online/algo/data-structure/binary-tree-part2/#%E9%80%9A%E8%BF%87%E5%90%8E%E5%BA%8F%E5%92%8C%E5%89%8D%E5%BA%8F%E9%81%8D%E5%8E%86%E7%BB%93%E6%9E%9C%E6%9E%84%E9%80%A0%E4%BA%8C%E5%8F%89%E6%A0%91
        if not inorder or not postorder:
            return

        root_val = postorder.pop()
        root = TreeNode(root_val)
        index = inorder.index(root_val)

        root.right = self.buildTree(inorder[index + 1 :], postorder)
        root.left = self.buildTree(inorder[:index], postorder)

        return root


# @lc code=end
