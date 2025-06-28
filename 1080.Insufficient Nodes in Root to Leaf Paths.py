#
# @lc app=leetcode id=1080 lang=python3
# @lcpr version=30201
#
# [1080] Insufficient Nodes in Root to Leaf Paths
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
    def sufficientSubset(
        self, root: Optional[TreeNode], limit: int
    ) -> Optional[TreeNode]:
        if not root:
            return None
        if not root.left and not root.right:
            return root if root.val >= limit else None

        new_limit = limit - root.val

        root.left = self.sufficientSubset(root.left, new_limit)
        root.right = self.sufficientSubset(root.right, new_limit)

        if root.left or root.right:
            return root
        else:
            return None


# @lc code=end


#
# @lcpr case=start
# [1,2,3,4,-99,-99,7,8,9,-99,-99,12,13,-99,14]\n1\n
# @lcpr case=end

# @lcpr case=start
# [5,4,8,11,null,17,4,7,1,null,null,5,3]\n22\n
# @lcpr case=end

# @lcpr case=start
# [1,2,-3,-5,null,4,null]\n-1\n
# @lcpr case=end

#
