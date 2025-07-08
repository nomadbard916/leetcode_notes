#
# @lc app=leetcode id=1379 lang=python3
# @lcpr version=30201
#
# [1379] Find a Corresponding Node of a Binary Tree in a Clone of That Tree
#

# @lc code=start
# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def getTargetCopy(
        self,
        original: Optional[TreeNode],
        cloned: Optional[TreeNode],
        target: Optional[TreeNode],
    ) -> Optional[TreeNode]:
        # Base case: if we've reached a null node, return None
        if not original or not cloned:
            return None

        # If we found the target node in the original tree,
        # return the corresponding node in the cloned tree
        if original is target:
            return cloned

        # Recursively search in the left subtree
        left_result = self.getTargetCopy(original.left, cloned.left, target)
        if left_result:
            return left_result

        # Recursively search in the right subtree
        right_result = self.getTargetCopy(original.right, cloned.right, target)
        return right_result


# @lc code=end


#
# @lcpr case=start
# [7,4,3,null,null,6,19]\n3\n
# @lcpr case=end

# @lcpr case=start
# [7]\n7\n
# @lcpr case=end

# @lcpr case=start
# [8,null,6,null,5,null,4,null,3,null,2,null,1]\n4\n
# @lcpr case=end

#
