#
# @lc app=leetcode id=98 lang=python3
#
# [98] Validate Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def DFS(root, min, max):
            # traverse all the way into void and it's sure to be valid
            if not root:
                return True

            # a BST's children values must be within limited upper & lower bounds
            if root.val >= max or root.val <= min:
                return False

            return DFS(root.left, min, root.val) and DFS(root.right, root.val, max)

        # at first the real min/max are unknown, so let's fake +-inf as min/max
        return DFS(root, float("-INF"), float("INF"))


# @lc code=end
