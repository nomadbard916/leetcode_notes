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

        def dfs(node: Optional[TreeNode]) -> int:
            if not node:
                return 0

            left_path = dfs(node.left)
            right_path = dfs(node.right)

            # * post order logic
            left_extend = 0
            right_extend = 0

            if node.left and node.left.val == node.val:
                left_extend = left_path + 1
            if node.right and node.right.val == node.val:
                right_extend = right_path + 1

            self.max_path = max(self.max_path, left_extend + right_extend)

            return max(left_extend, right_extend)

        dfs(root)

        return self.max_path


# @lc code=end


#
# @lcpr case=start
# [5,4,5,1,1,null,5]\n
# @lcpr case=end

# @lcpr case=start
# [1,4,5,4,4,null,5]\n
# @lcpr case=end

#
