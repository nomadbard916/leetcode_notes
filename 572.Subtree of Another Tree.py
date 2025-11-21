#
# @lc app=leetcode id=572 lang=python3
# @lcpr version=30201
#
# [572] Subtree of Another Tree
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
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # nouns and keywords
        """
        - noun
        subtree, escendants
        - verb
        consist
        """

        # pattern keywords
        """
        subtree
        same structure and node values
        """

        # constraints
        """
        root node number 1~2000
        subRoot node number 1~1000
        """

        # look for root of subRoot
        # pre-order traversal
        def is_same_tree(p: Optional[TreeNode], q: Optional[TreeNode]):
            if p is None and q is None:
                return True

            if p is None or q is None:
                return False

            if p.val != q.val:
                return False

            return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)

        # base cases
        if subRoot is None:
            return True

        if root is None:
            return False

        if is_same_tree(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)


# @lc code=end


#
# @lcpr case=start
# [3,4,5,1,2]\n[4,1,2]\n
# @lcpr case=end

# @lcpr case=start
# [3,4,5,1,2,null,null,null,null,0]\n[4,1,2]\n
# @lcpr case=end

#
