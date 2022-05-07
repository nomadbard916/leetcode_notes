#
# @lc app=leetcode id=513 lang=python3
#
# [513] Find Bottom Left Tree Value
#

# @lc code=start
# Definition for a binary tree node.
import collections
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        # BFS
        queue = collections.deque([root])
        ans = None

        while queue:
            size = len(queue)
            for _ in range(size):
                ans = current_node = queue.popleft()
                # make sure left is always on right
                if current_node.right:
                    queue.append(current_node.right)

                if current_node.left:
                    queue.append(current_node.left)
        return ans.val


# @lc code=end
