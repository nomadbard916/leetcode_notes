#
# @lc app=leetcode id=979 lang=python3
# @lcpr version=30201
#
# [979] Distribute Coins in Binary Tree
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
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        # * Approach: Post-order DFS
        # - For each node, calculate how many coins it needs or has excess
        # - Move coins up to parent, counting each move
        moves = 0

        def dfs(node: Optional[TreeNode]) -> int:
            """
            Returns the net coin flow from this subtree to its parent.
            Positive = excess coins flowing up
            Negative = deficit coins needed from parent
            """
            nonlocal moves
            if not node:
                return 0

            left_flow = dfs(node.left)
            right_flow = dfs(node.right)

            # * post order logic
            # Count moves: absolute value of flow = number of moves
            moves += abs(left_flow) + abs(right_flow)

            # Calculate net flow from current node to its parent
            # = coins_in_node + coins_from_children - coins_needed
            # = node.val + left_flow + right_flow - 1
            return node.val + left_flow + right_flow - 1

        dfs(root)

        return moves


# @lc code=end


#
# @lcpr case=start
# [3,0,0]\n
# @lcpr case=end

# @lcpr case=start
# [0,3,0]\n
# @lcpr case=end

#
