#
# @lc app=leetcode id=1026 lang=python3
# @lcpr version=30104
#
# [1026] Maximum Difference Between Node and Ancestor
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
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def dfs(node: TreeNode, min_val: int, max_val: int) -> int:
            """
            DFS helper function that tracks min and max values along the path.

            Args:
                node: Current node being processed
                min_val: Minimum value encountered from root to current node
                max_val: Maximum value encountered from root to current node

            Returns:
                Maximum difference found in this subtree
            """
            # Base case: if node is None, return 0
            if not node:
                return 0

            # Calculate the maximum difference at current node
            # This is the max of:
            # 1. Current node value - minimum ancestor value
            # 2. Maximum ancestor value - current node value
            current_diff = max(abs(node.val - min_val), abs(node.val - max_val))

            # Update min and max values for the next level
            new_min = min(min_val, node.val)
            new_max = max(max_val, node.val)

            # Recursively explore left and right subtrees
            left_diff = dfs(node.left, new_min, new_max)
            right_diff = dfs(node.right, new_min, new_max)

            # Return the maximum difference found
            return max(current_diff, left_diff, right_diff)

        # Start DFS with root value as both min and max
        return dfs(root, root.val, root.val)


# @lc code=end


#
# @lcpr case=start
# [8,3,10,1,6,null,14,null,null,4,7,13]\n
# @lcpr case=end

# @lcpr case=start
# [1,null,2,null,0,3]\n
# @lcpr case=end

#
