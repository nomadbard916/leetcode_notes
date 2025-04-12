#
# @lc app=leetcode id=199 lang=python3
#
# [199] Binary Tree Right Side View
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
    def rightSideView(self, root: TreeNode) -> List[int]:
        # see only right nodes
        if root is None:
            return []

        ans = []

        def DFS(root: TreeNode | None, current_level: int):
            if root is None:
                return

            # Using pre-order traversal (root, right, left) ensures that:
            # 1. We process the rightmost node of each level first
            # 2. We only add a node to 'ans' if its level is not yet represented
            # This guarantees that 'ans' will contain only the rightmost nodes
            if current_level == len(ans):
                ans.append(root.val)

            DFS(root.right, current_level + 1)
            DFS(root.left, current_level + 1)

        DFS(root, 0)

        return ans

        # sol2: iterate with level order, then print the last element of each level.
        # see 102


# @lc code=end
