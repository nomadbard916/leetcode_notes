#
# @lc app=leetcode id=101 lang=python3
#
# [101] Symmetric Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        # for every node:
        # left child s right must be equal to right child's left
        # and left child's left must be equal to right child's right

        # kind of BFS
        def traverse(l_child, r_child):
            # symmetric, as both children are None
            if not l_child and not r_child:
                return True
            # asymmetric, as it's one-sided
            if not l_child or not r_child:
                return False

            if l_child and r_child and l_child.val == r_child.val:
                return traverse(l_child.right, r_child.left) and traverse(
                    l_child.left, r_child.right
                )
            return False

        if root:
            return traverse(root.left, root.right)
        else:
            return True


# @lc code=end

