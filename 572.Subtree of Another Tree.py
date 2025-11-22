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
        subtree, descendants
        - verb
        consist
        """

        # pattern keywords
        """
        subtree -> recursion/dfs
        same structure and node values -> same tree comparison
        """

        # constraints
        """
        root node number 1~2000
        subRoot node number 1~1000
        two binary trees -> dual tree traversal
        subtrees must match exactly
        """

        # category
        """
        tree -> traversal -> comparison
        sub-problem recursively
        """

        # tricky
        """
        subtree -> must include all descendants down to leaves
        """

        # look for root of subRoot
        # pre-order traversal
        def is_same_tree(p: Optional[TreeNode], q: Optional[TreeNode]):
            """
            Check if two trees are exactly identical (structure + values).
            This is essentially LeetCode 100: Same Tree.
            """
            # Both empty → same
            if p is None and q is None:
                return True

            # One empty, one not → different
            if p is None or q is None:
                return False

            # Both non-empty → check value and recurse on children
            if p.val != q.val:
                return False

            return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)

        # base cases
        if subRoot is None:
            return True

        if root is None:
            return False

        # Check if current position matches, OR check left/right subtrees
        if is_same_tree(root, subRoot):
            return True

        # Recursively check if subRoot is in left or right subtree of root
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

        # Time and Space Complexity
        # Complexity | Value | Explanation
        # Time | O (n × m) | For each of n nodes in root, we might compare up to m nodes of subRoot
        # Space | O(h₁ + h₂) | Recursion stack depth: height of root + height of subRoot
        # Where:
        # n = number of nodes in root
        # m = number of nodes in subRoot
        # h₁, h₂ = heights of respective trees

        # Worst case: Both trees are skewed (like linked lists) → O(n × m) time, O(n + m) space


# @lc code=end


#
# @lcpr case=start
# [3,4,5,1,2]\n[4,1,2]\n
# @lcpr case=end

# @lcpr case=start
# [3,4,5,1,2,null,null,null,null,0]\n[4,1,2]\n
# @lcpr case=end

#
