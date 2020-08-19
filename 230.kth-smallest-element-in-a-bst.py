#
# @lc app=leetcode id=230 lang=python3
#
# [230] Kth Smallest Element in a BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        # brute force: traverse postorderly the tree and put elements into a t_list, then fetch t_list[-k]
        # BST definition: any left child node must be smaller than its root node, and any right must be bigger than root
        # inorder traversal and record k ordering in the process
        # when to update k value?

        global ans, count
        ans = 0
        count = 0

        def traverse(root):
            # sanity check
            if root is None:
                return

            traverse(root.left)

            # in BST, as left child node must be smaller than parent rood node, the traversal count should be recorded here
            global count, ans
            count += 1
            if count == k:
                ans = root.val

            traverse(root.right)

        traverse(root)

        return ans


# @lc code=end

