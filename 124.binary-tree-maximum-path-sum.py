#
# @lc app=leetcode id=124 lang=python3
#
# [124] Binary Tree Maximum Path Sum
#

# @lc code=start
# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # see also #113
    # integer instead of float('int')
    ans = -(2**99)

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            # keep iterating left and right recursively,
            # and update global max when necessary
            self.ans = max(self.ans, max(left, 0) + max(right, 0) + node.val)
            # choose only the bigger side
            return max(left, right, 0) + node.val

        dfs(root)
        return self.ans


# @lc code=end
