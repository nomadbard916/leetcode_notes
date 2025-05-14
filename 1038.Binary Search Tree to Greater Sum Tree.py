#
# @lc app=leetcode id=1038 lang=python3
# @lcpr version=30104
#
# [1038] Binary Search Tree to Greater Sum Tree
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
    def __init__(self) -> None:
        self.sum = 0

    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # totally the same as 538
        def traverse(root):
            if root is None:
                return

            traverse(root.right)
            # * in-order operations
            # make greater sum
            self.sum += root.val
            # convert BST to greater sum
            root.val = self.sum

            traverse(root.left)

        traverse(root)
        return root


# @lc code=end


#
# @lcpr case=start
# [4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]\n
# @lcpr case=end

# @lcpr case=start
# [0,null,1]\n
# @lcpr case=end

#
