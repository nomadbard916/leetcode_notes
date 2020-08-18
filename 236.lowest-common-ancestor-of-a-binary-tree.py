#
# @lc app=leetcode id=236 lang=python3
#
# [236] Lowest Common Ancestor of a Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        # root for left child tree and right child tree when p and q are found
        # when to return root node?
        # may need to cut when one of p ,q is found

        # when traversing preorderly with a tree-point tree:
        # if p, q is root.left or root.right: root is common ancestor
        # if p is root or q is root: found and go to previous layer

        # traversing the whole tree, from the most basic child tree (even thinking of leaf node) then recursively going up

        # preorder
        # ending condition: out of bound
        if root is None:
            return

        # ending condition: current node is one of the matches
        if root == p or root == q:
            return root

        #  go to next levels and recursively check if direct children match
        left_search = self.lowestCommonAncestor(root.left, p, q)
        right_search = self.lowestCommonAncestor(root.right, p, q)

        # searching on a child tree must have four resulting conditions:
        # out of bound
        if left_search is None and right_search is None:
            return  # to previous level as searching reaches leaf node and nothing found

        # bubbling up when target found
        # the node is p or q
        if left_search is not None and right_search is not None:
            return root

        if left_search is None:
            return right_search
        else:
            return left_search


# @lc code=end

