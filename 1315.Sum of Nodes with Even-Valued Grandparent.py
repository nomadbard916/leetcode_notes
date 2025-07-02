#
# @lc app=leetcode id=1315 lang=python3
# @lcpr version=30201
#
# [1315] Sum of Nodes with Even-Valued Grandparent
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
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        # ! sol1: DFS
        def dfs(node: Optional[TreeNode], parent_val: int, grandparent_val: int) -> int:
            if not node:
                return 0

            # initialize sum for current subtree
            current_sum = 0

            if grandparent_val != -1 and grandparent_val % 2 == 0:
                current_sum += node.val

            left_sum = dfs(node.left, node.val, parent_val)
            right_sum = dfs(node.right, node.val, parent_val)

            return current_sum + left_sum + right_sum

        return dfs(root, -1, -1)


# @lc code=end


#
# @lcpr case=start
# [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]\n
# @lcpr case=end

# @lcpr case=start
# [1]\n
# @lcpr case=end

#
