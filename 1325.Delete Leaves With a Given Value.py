#
# @lc app=leetcode id=1325 lang=python3
# @lcpr version=30201
#
# [1325] Delete Leaves With a Given Value
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
    def removeLeafNodes(
        self, root: Optional[TreeNode], target: int
    ) -> Optional[TreeNode]:
        # ! post-order traversal
        # Base case: if current node is None, return None
        if not root:
            return None

        # Recursively process left and right subtrees first
        # This ensures we work from bottom to top (post-order traversal)
        root.left = self.removeLeafNodes(root.left, target)
        root.right = self.removeLeafNodes(root.right, target)

        # After processing children, check if current node should be removed
        is_leaf = not root.left and not root.right
        meet_target = root.val == target
        if is_leaf and meet_target:
            return None

        return root


# @lc code=end


#
# @lcpr case=start
# [1,2,3,2,null,2,4]\n2\n
# @lcpr case=end

# @lcpr case=start
# [1,3,3,3,2]\n3\n
# @lcpr case=end

# @lcpr case=start
# [1,2,null,2,null,2]\n2\n
# @lcpr case=end

#
