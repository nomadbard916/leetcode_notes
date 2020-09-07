from typing import List

#
# @lc app=leetcode id=145 lang=python3
#
# [145] Binary Tree Postorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        ans = []

        def DFS(root=root):
            if root is None:
                return None

            DFS(root.left)
            DFS(root.right)

            ans.append(root.val)

        DFS()

        return ans


# @lc code=end

