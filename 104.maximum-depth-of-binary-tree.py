#
# @lc app=leetcode id=104 lang=python3
#
# [104] Maximum Depth of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        # get the bigger depth of left child tree and right child tree, then +1 to count in the root node

        # ending condition: out of bound
        if root is None:
            return 0

        l_depth = self.maxDepth(root.left)
        r_depth = self.maxDepth(root.right)

        # essentiall postorder traversal, i.e. result of current node
        max_children_depth = max(l_depth, r_depth)

        # the current node itself + deedpest children depth
        return 1 + max_children_depth


# @lc code=end

