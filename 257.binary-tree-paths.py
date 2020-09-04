#
# @lc app=leetcode id=257 lang=python3
#
# [257] Binary Tree Paths
#

# @lc code=start
# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        ans = []

        if root is None:
            return ans

        def DFS(root=root, current_path: str = str(root.val)):
            if root.left is None and root.right is None:
                ans.append(current_path)
                return

            if root.left:
                DFS(root.left, current_path + "->" + str(root.left.val))
            if root.right:
                DFS(root.right, current_path + "->" + str(root.right.val))

        DFS()

        return ans


# @lc code=end

