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
    result = None
    builder = []

    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        def traverse(node: TreeNode):
            if not node:
                return

            # Append the current character
            self.builder.append(chr(ord("a") + node.val))

            # If it's a leaf, build the reversed string and compare
            if not node.left and not node.right:
                current_str = "".join(reversed(self.builder))
                if self.result is None or current_str < self.result:
                    self.result = current_str

            # Continue traversing child nodes
            traverse(node.left)
            traverse(node.right)

            # Remove the last character to backtrack
            self.builder.pop()

        traverse(root)
        return self.result if self.result is not None else ""


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
