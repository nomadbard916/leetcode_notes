#
# @lc app=leetcode id=230 lang=python3
#
# [230] Kth Smallest Element in a BST
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    ans: int = 0
    count: int = 0

    def kthSmallest(self, root: TreeNode, k: int) -> int:
        # brute force:
        # traverse postorderly the tree and put elements into a t_list,
        # then fetch t_list[-k]

        # in-order traversal for BST, and record k ordering in the process
        # when to update k value?

        def DFS(root):
            if root is None:
                return

            DFS(root.left)

            # in BST, as left child node must be smaller than parent rood node,
            # the traversal count should be recorded here
            self.count += 1
            if self.count == k:
                self.ans = root.val

            DFS(root.right)

        DFS(root)

        return self.ans


# @lc code=end
