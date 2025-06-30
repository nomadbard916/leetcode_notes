#
# @lc app=leetcode id=814 lang=python3
# @lcpr version=30201
#
# [814] Binary Tree Pruning
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
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        root.left = self.pruneTree(root.left)
        root.right = self.pruneTree(root.right)

        # * post order logic
        if root.val == 1 or root.left or root.right:
            return root

        return None


# @lc code=end


#
# @lcpr case=start
# [1,null,0,0,1]\n
# @lcpr case=end

# @lcpr case=start
# [1,0,1,0,0,0,1]\n
# @lcpr case=end

# @lcpr case=start
# [1,1,0,1,1,0,1,0]\n
# @lcpr case=end

#
