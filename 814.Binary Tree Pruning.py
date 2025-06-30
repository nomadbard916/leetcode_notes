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
        # * post order traversal, see also 1080
        # base case: already into emptiness
        if not root:
            return

        # recursively prune left and right subtrees first,
        # process children before parent
        root.left = self.pruneTree(root.left)
        root.right = self.pruneTree(root.right)

        # * post order logic
        # After pruning children, check if current node should be kept
        # Keep the node if:
        # 1. The node's value is 1, OR
        # 2. It has at least one non-null child (meaning subtree contains 1s)
        if root.val == 1 or (root.left or root.right):
            return root

        # If node value is 0 AND both children are None, prune this node
        return None

        # Complexity Analysis

        # Time Complexity: O(n) where n is the number of nodes
        # We visit each node exactly once
        # Each visit does constant work

        # Space Complexity: O(h) where h is the height of the tree
        # Recursion stack depth equals tree height
        # Best case: O(log n) for balanced tree
        # Worst case: O(n) for skewed tree


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
