from typing import List

#
# @lc app=leetcode id=94 lang=python3
#
# [94] Binary Tree Inorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        ans = []

        def DFS(root=root):
            if root is None:
                return

            DFS(root.left)

            ans.append(root.val)

            DFS(root.right)

        DFS()

        return ans


# @lc code=end

