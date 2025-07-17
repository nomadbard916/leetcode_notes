#
# @lc app=leetcode id=865 lang=python3
# @lcpr version=30201
#
# [865] Smallest Subtree with all the Deepest Nodes
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
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node: Optional[TreeNode]) -> tuple[Optional[TreeNode], int]:
            if not node:
                return None, 0
            left_subtree, left_depth = dfs(node.left)
            right_subtree, right_depth = dfs(node.right)

            if left_depth > right_depth:
                return left_subtree, left_depth + 1
            elif left_depth < right_depth:
                return right_subtree, right_depth + 1
            else:
                return node, left_depth + 1

        subtree_root, _ = dfs(root)

        return subtree_root


# @lc code=end


#
# @lcpr case=start
# [3,5,1,6,2,0,8,null,null,7,4]\n
# @lcpr case=end

# @lcpr case=start
# [1]\n
# @lcpr case=end

# @lcpr case=start
# [0,1,3,null,2]\n
# @lcpr case=end

#
