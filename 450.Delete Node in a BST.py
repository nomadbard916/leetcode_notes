#
# @lc app=leetcode id=450 lang=python3
# @lcpr version=30104
#
# [450] Delete Node in a BST
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
    def getMin(self, node: TreeNode) -> TreeNode:
        # for BST, ths left-most child node is the smallest node
        while node.left is not None:
            node = node.left
        return node

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return None

        # * search phase first
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        # * found: root.val == key
        else:
            # * start deleting, but cannot break the BST. 3 possibilities:
            # 1: it's the leaf node, just remove it
            # 2: only one child node, then just let the child substitute itself
            if root.left is None:
                return root.right
            if root.right is None:
                return root.left
            # 3: the root has two children nodes.
            # in order not to break BST, find the biggest node in left sub tree,
            # or the smallest child node in right sub tree;
            # to subsitute it.
            minNode = self.getMin(root.right)
            # delete the smallest node in right tree
            root.right = self.deleteNode(root.right, minNode.val)
            # take the smallest node in right sub tree to subsitute the root
            minNode.left = root.left
            minNode.right = root.right
            root = minNode
        return root


# @lc code=end


#
# @lcpr case=start
# [5,3,6,2,4,null,7]\n3\n
# @lcpr case=end

# @lcpr case=start
# [5,3,6,2,4,null,7]\n0\n
# @lcpr case=end

# @lcpr case=start
# []\n0\n
# @lcpr case=end

#
