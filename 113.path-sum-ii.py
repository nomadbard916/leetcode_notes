#
# @lc app=leetcode id=113 lang=python3
#
# [113] Path Sum II
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
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        paths = []

        if root is None:
            return paths

        def DFS(current_path: list, root=root, current_sum=0):
            if root is None:
                return

            # preorder
            updated_path = current_path + [root.val]
            updated_sum = current_sum + root.val

            # ending condition
            if root.left is None and root.right is None and updated_sum == sum:
                paths.append(updated_path)
                return

            if root.left:
                DFS(updated_path, root.left, updated_sum)
            if root.right:
                DFS(updated_path, root.right, updated_sum)

        current_path = []
        DFS(current_path)

        return paths


# @lc code=end
