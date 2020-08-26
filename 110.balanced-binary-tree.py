#
# @lc app=leetcode id=110 lang=python3
#
# [110] Balanced Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def height(root):
            if root is None:
                return 0
            return max(height(root.left), height(root.right)) + 1

        if root is None:
            return True

        if abs(height(root.left) - height(root.right)) > 1:
            return False

        return self.isBalanced(root.left) and self.isBalanced(root.right)


# @lc code=end

