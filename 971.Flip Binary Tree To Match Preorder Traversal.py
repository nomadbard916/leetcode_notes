#
# @lc app=leetcode id=971 lang=python3
# @lcpr version=30201
#
# [971] Flip Binary Tree To Match Preorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flipMatchVoyage(self, root: Optional[TreeNode], voyage: List[int]) -> List[int]:
        self.flipped = []
        self.index = 0

        def dfs(node: Optional[TreeNode]) -> bool:
            if not node:
                return True

            if self.index >= len(voyage) or node.val != voyage[self.index]:
                return False

            self.index += 1

            if not node.left and not node.right:
                return True

            if not node.left:
                return dfs(node.right)
            if not node.right:
                return dfs(node.left)

            if self.index < len(voyage) and node.left.val == voyage[self.index]:
                return dfs(node.left) and dfs(node.right)
            elif self.index < len(voyage) and node.right.val == voyage[self.index]:
                self.flipped.append(node.val)
                return dfs(node.right) and dfs(node.left)
            else:
                return False

        if dfs(root):
            return self.flipped

        return [-1]


# @lc code=end


#
# @lcpr case=start
# [1,2]\n[2,1]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3]\n[1,3,2]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3]\n[1,2,3]\n
# @lcpr case=end

#
