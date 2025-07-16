#
# @lc app=leetcode id=669 lang=python3
# @lcpr version=30201
#
# [669] Trim a Binary Search Tree
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
    def trimBST(
        self, root: Optional[TreeNode], low: int, high: int
    ) -> Optional[TreeNode]:
        #  * The key insight is leveraging the BST property:
        # for any node, all values in the left subtree are smaller,
        # and all values in the right subtree are larger.

        #  Notice how we're not just marking nodes for deletion -
        # we're actually rebuilding the tree structure by updating parent-child relationships.

        if not root:
            return None

        # If current node's value is less than low bound,
        # we need to discard this node and its left subtree
        # because all values in left subtree are even smaller
        if root.val < low:
            return self.trimBST(root.right, low, high)

        # If current node's value is greater than high bound,
        # we need to discard this node and its right subtree
        # because all values in right subtree are even larger
        if root.val > high:
            return self.trimBST(root.left, low, high)

        # * post order logic
        # node.val in range:
        # If current node's value is within [low, high],
        # we keep this node and recursively trim both subtrees
        root.left = self.trimBST(root.left, low, high)
        root.right = self.trimBST(root.right, low, high)

        return root

        # Time and Space Complexity
        # Time Complexity:
        # O(n) where n is the number of nodes in the tree. In the worst case, we visit every node once.
        # Space Complexity:
        # O(h) where h is the height of the tree, due to the recursion stack.
        # In the worst case (skewed tree), this could be O(n).


# @lc code=end


#
# @lcpr case=start
# [1,0,2]\n1\n2\n
# @lcpr case=end

# @lcpr case=start
# [3,0,4,null,2,null,null,1]\n1\n3\n
# @lcpr case=end

#
