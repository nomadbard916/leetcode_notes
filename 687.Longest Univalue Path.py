#
# @lc app=leetcode id=687 lang=python3
# @lcpr version=30201
#
# [687] Longest Univalue Path
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
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        self.max_path = 0

        # For each node, we need to consider two types of paths:
        # - Single-direction path: Going down from current node to descendants (returned by our function)
        # - Through-node path: Combining left and right paths that pass through current node (used to update global maximum)

        def dfs(node: Optional[TreeNode]) -> int:
            if not node:
                return 0

            left_path_len = dfs(node.left)
            right_path_len = dfs(node.right)

            # * post order logic
            left_extend_len = 0
            right_extend_len = 0

            if node.left and node.left.val == node.val:
                left_extend_len = left_path_len + 1
            if node.right and node.right.val == node.val:
                right_extend_len = right_path_len + 1

            self.max_path = max(self.max_path, left_extend_len + right_extend_len)

            return max(left_extend_len, right_extend_len)

        dfs(root)

        return self.max_path

        # complexities
        # Time Complexity: O(n) - We visit each node exactly once
        # Space Complexity: O(h) - Recursion stack depth equals tree height


# @lc code=end


#
# @lcpr case=start
# [5,4,5,1,1,null,5]\n
# @lcpr case=end

# @lcpr case=start
# [1,4,5,4,4,null,5]\n
# @lcpr case=end

#
