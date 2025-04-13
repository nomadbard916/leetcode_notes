#
# @lc app=leetcode id=988 lang=python3
# @lcpr version=30104
#
# [988] Smallest String Starting From Leaf
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
    current_path = ""
    res = None

    def traverse(self, root):
        # the pre-order operation is used to construct the path as the traversal goes deeper,
        # and the post-order operation is used to backtrack and maintain the correct path state.
        # This combination is necessary for the specific problem of finding the smallest string from leaf to root.
        if root is None:
            return

        ASCII_value_a = ord("a")

        if root.left is None and root.right is None:
            self.current_path = chr(ASCII_value_a + root.val) + self.current_path

            if self.res is None:
                self.res = self.current_path

            # update res if it exceeds current potential res
            if self.res > self.current_path:
                self.res = self.current_path

            # Remove current node's character from the path
            self.current_path = self.current_path[1:]
            return

        # Pre-order: Add current node's character to the path
        #  This ensures that as you go deeper into the tree,
        # the path is constructed in the order from the current node down to the leaf.
        self.current_path = chr(ASCII_value_a + root.val) + self.current_path

        self.traverse(root.left)
        self.traverse(root.right)

        # Post-order: Remove current node's character from the path
        #  This is necessary to ensure that when the traversal backtracks to the parent node,
        # the path reflects the correct state without the current node's character.
        self.current_path = self.current_path[1:]
        return

    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str | None:
        self.traverse(root)
        return self.res


# @lc code=end


#
# @lcpr case=start
# [0,1,2,3,4,3,4]\n
# @lcpr case=end

# @lcpr case=start
# [25,1,3,1,3,0,2]\n
# @lcpr case=end

# @lcpr case=start
# [2,2,1,null,1,0,null,0]\n
# @lcpr case=end

#
