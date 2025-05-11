#
# @lc app=leetcode id=105 lang=python3
#
# [105] Construct Binary Tree from Preorder and Inorder Traversal
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
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # TODO: Q889 with framework from labuladong
        # https://labuladong.online/algo/data-structure/binary-tree-part2/#%E9%80%9A%E8%BF%87%E5%90%8E%E5%BA%8F%E5%92%8C%E5%89%8D%E5%BA%8F%E9%81%8D%E5%8E%86%E7%BB%93%E6%9E%9C%E6%9E%84%E9%80%A0%E4%BA%8C%E5%8F%89%E6%A0%91
        if not preorder or not inorder:
            return None

        root_val = preorder.pop(0)
        root = TreeNode(root_val)
        root_index = inorder.index(root_val)
        root.left = self.buildTree(preorder, inorder[:root_index])
        root.right = self.buildTree(preorder, inorder[root_index + 1 :])

        return root


# @lc code=end
