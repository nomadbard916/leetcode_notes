#
# @lc app=leetcode id=662 lang=python3
#
# [662] Maximum Width of Binary Tree
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
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # level order traversal, with id of node in tree recorded
        # as every null node should be seen as 'invisible' as the problem stated

        # no need to worry about integer overflow after 64 levels,
        # as it's guaranteed to be 32-bit signed integer

        q = collections.deque()
        q.append((root, 1))
        ans = 0

        while q:
            first_node_id = q[0][1]
            last_node_id = q[-1][1]
            level_width = last_node_id - first_node_id + 1

            ans = max(level_width, ans)

            for _ in range(len(q)):
                node, node_id = q.popleft()
                if node.left:
                    q.append((node.left, node_id * 2))
                if node.right:
                    q.append((node.right, node_id * 2 + 1))

        return ans

        # WRONG sol2: level order traversal
        # calculate level width and keep updating
        # however, the actual level node count is not the real width


# @lc code=end
