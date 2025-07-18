#
# @lc app=leetcode id=951 lang=python3
# @lcpr version=30201
#
# [951] Flip Equivalent Binary Trees
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
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        # we can define a flip operation as follows: choose any node, and swap the left and right child subtrees.
        # A binary tree X is flip equivalent to a binary tree Y if and only if
        # we can make X equal to Y after some number of flip operations.

        # Base case: both nodes are None
        if not root1 and not root2:
            return True
        # Base case: one node is None, the other is not
        if not root1 or not root2:
            return False
        # Base case: values are different
        if root1.val != root2.val:
            return False

        # we don't include below condition
        # if root1.val == root2.val:
        #     return True
        # Just because two nodes have the same value doesn't mean the entire subtrees rooted at those nodes are flip equivalent!

        # Recursive case: check both possibilities
        # Option 1: No flip needed (left matches left, right matches right)
        no_flip = self.flipEquiv(root1.left, root2.left) and self.flipEquiv(
            root1.right, root2.right
        )
        # Option 2: Flip needed (left matches right, right matches left)
        flip = self.flipEquiv(root1.left, root2.right) and self.flipEquiv(
            root1.right, root2.left
        )

        # Trees are flip equivalent if either option works
        return no_flip or flip

        # Time and Space Complexity

        # Time Complexity: O(min(N1, N2)) where N1 and N2 are the number of nodes in the two trees

        # We visit each node at most once
        # We stop early if trees have different structures

        # Space Complexity: O(min(H1, H2)) where H1 and H2 are the heights of the two trees

        # This is the maximum recursion depth
        # In the worst case (skewed tree), this could be O(N)
        # In the best case (balanced tree), this is O(log N)


# @lc code=end


#
# @lcpr case=start
# [1,2,3,4,5,6,null,null,null,7,8]\n[1,3,2,null,6,4,5,null,null,null,null,8,7]\n
# @lcpr case=end

# @lcpr case=start
# []\n[]\n
# @lcpr case=end

# @lcpr case=start
# []\n[1]\n
# @lcpr case=end

#
