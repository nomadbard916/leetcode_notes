#
# @lc app=leetcode id=235 lang=python3
#
# [235] Lowest Common Ancestor of a Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
from typing import Union


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: Union[TreeNode, None], p: "TreeNode", q: "TreeNode"
    ) -> Union[TreeNode, None]:
        # definition of BST:
        # any left node must be smaller than its root, any right bigger than root
        if root is None:
            return

        # if both smaller than root:
        # common ancestor must be in left child tree
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)

        # if both bigger than root:
        # common ancestor must be in right child tree
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)

        # if one bigger and the other smaller:
        # they must be on different sides of root, so only root can be common ancestor
        return root


# @lc code=end
