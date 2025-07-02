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
        non_existing_node_val = -1

        def dfs(node: Optional[TreeNode], parent_val: int, grandparent_val: int) -> int:
            if not node:
                return 0

            # initialize sum for current subtree
            current_sum = 0

            grandparent_exists = grandparent_val != non_existing_node_val
            grandparent_is_even = grandparent_val % 2 == 0
            if grandparent_exists and grandparent_is_even:
                current_sum += node.val

            left_sum = dfs(node.left, node.val, parent_val)
            right_sum = dfs(node.right, node.val, parent_val)

            return current_sum + left_sum + right_sum

        return dfs(root, non_existing_node_val, non_existing_node_val)


# @lc code=end


#
# @lcpr case=start
# [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]\n
# @lcpr case=end

# @lcpr case=start
# [1]\n
# @lcpr case=end

#
