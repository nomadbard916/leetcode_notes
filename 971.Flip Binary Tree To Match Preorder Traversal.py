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
        # Store nodes that we flip
        self.flipped = []
        # Track current position in voyage
        self.index = 0

        def dfs(node: Optional[TreeNode]) -> bool:
            if not node:
                return True

            # Check if current node matches expected value in voyage
            if self.index >= len(voyage) or node.val != voyage[self.index]:
                return False

            self.index += 1

            # If this is a leaf node, we're done with this subtree
            if not node.left and not node.right:
                return True

            # If only one child exists, process it normally
            if not node.left:
                return dfs(node.right)
            if not node.right:
                return dfs(node.left)

            # Both children exist - check if we need to flip
            # Look at the next value in voyage to decide
            if self.index < len(voyage):
                curr_voyage_val = voyage[self.index]
                if node.left.val == curr_voyage_val:
                    # Left child matches next expected value - no flip needed
                    return dfs(node.left) and dfs(node.right)
                elif node.right.val == curr_voyage_val:
                    # Right child matches next expected value - need to flip
                    self.flipped.append(node.val)
                    return dfs(node.right) and dfs(node.left)
                else:
                    # Neither child matches - impossible to match voyage
                    return False
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
