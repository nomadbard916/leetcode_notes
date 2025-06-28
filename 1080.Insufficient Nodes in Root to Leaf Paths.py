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
        # ! sol1:
        # Core Insight: We need to work bottom-up (post-order traversal)
        # because we can only determine if a node should be removed after we know about its children's sufficiency.

        # * Base case: if node is None, return None
        if not root:
            return None
        # * If this is a leaf node, check if current path sum meets the limit
        if not root.left and not root.right:
            # If leaf value is >= limit, keep it; otherwise remove it
            return root if root.val >= limit else None

        # For internal nodes, recursively process children
        # Update limit by subtracting current node's value
        new_limit = limit - root.val

        # Recursively process left and right subtrees
        root.left = self.sufficientSubset(root.left, new_limit)
        root.right = self.sufficientSubset(root.right, new_limit)

        # After processing children, check if current node should be kept
        # Keep the node if at least one child exists (meaning at least one
        # path through this node is sufficient)
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
