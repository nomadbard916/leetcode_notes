#
# @lc app=leetcode id=865 lang=python3
# @lcpr version=30201
#
# [865] Smallest Subtree with all the Deepest Nodes
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
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # * we need to find the Lowest Common Ancestor (LCA) of all the deepest nodes in the binary tree.

        # ! sol1: one-pass DFS (optimal)
        def dfs(node: Optional[TreeNode]) -> tuple[Optional[TreeNode], int]:
            if not node:
                return None, 0

            left_subtree, left_depth = dfs(node.left)
            right_subtree, right_depth = dfs(node.right)

            # * post order logic
            # If only one deepest node exists: That node itself is the answer
            if left_depth > right_depth:
                return left_subtree, left_depth + 1
            elif left_depth < right_depth:
                return right_subtree, right_depth + 1
            # both sides, LCA is the answer with either depth can do
            else:
                return node, left_depth + 1

        subtree_root, _ = dfs(root)

        return subtree_root

        # ! sol2: two-pass DFS, more intuitive but less efficient
        # first pass: find the max depth
        # second pass: find all deepest nodes and their LCA

        def find_max_depth(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            left_max_length = find_max_depth(node.left)
            right_max_length = find_max_depth(node.right)
            # * post order logic
            return 1 + max(left_max_length, right_max_length)

        def find_lca_of_deepest(
            node: Optional[TreeNode], curr_depth: int, max_depth: int
        ) -> TreeNode:
            if not node or curr_depth == max_depth:
                return node
            left_result = find_lca_of_deepest(node.left, curr_depth + 1, max_depth)
            right_result = find_lca_of_deepest(node.right, curr_depth + 1, max_depth)

            if left_result and right_result:
                return node

            return left_result or right_result

        max_depth = find_max_depth(root)
        return find_lca_of_deepest(root, 1, max_depth)

        # Time and Space Complexity

        # Solution 1 (One-Pass DFS):
        # Time Complexity: O(n) - visit each node once
        # Space Complexity: O(h) - recursion stack, where h is height of tree

        # Solution 2 (Two-Pass):
        # Time Complexity: O(n) - two passes through the tree
        # Space Complexity: O(h) - recursion stack


# @lc code=end


#
# @lcpr case=start
# [3,5,1,6,2,0,8,null,null,7,4]\n
# @lcpr case=end

# @lcpr case=start
# [1]\n
# @lcpr case=end

# @lcpr case=start
# [0,1,3,null,2]\n
# @lcpr case=end

#
