#
# @lc app=leetcode id=1448 lang=python3
# @lcpr version=30201
#
# [1448] Count Good Nodes in Binary Tree
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
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node: Optional[TreeNode], max_val: int) -> int:
            # Why This Dual Traversal Pattern with both Pre Order and Post Order is Necessary:
            # Information Flow in Two Directions:
            # 1 Downward Flow (Preorder):
            # - max_val information flows from parent to children
            # - Each node needs to know "what's the maximum value from root to my parent?"
            # 2 Upward Flow (Postorder):
            # - Count results flow from children back to parent
            # - Each node needs to know "how many good nodes are in my left and right subtrees?"
            #  * base case: if node is None, no good nodes
            if not node:
                return 0

            # * pre order logic:
            # Check if current node is good
            good_count = 0
            #  node is good if its value >= max value in path from root
            if node.val >= max_val:
                good_count = 1

            # Update max_val for children - it's the maximum of current max_val and current node's value
            new_max = max(max_val, node.val)

            # * post order logic
            # Recursively count good nodes in left and right subtrees with state propagation
            left_good_count = dfs(node.left, new_max)
            right_good_count = dfs(node.right, new_max)
            good_count += left_good_count + right_good_count

            return good_count

        # Start DFS from root with root's value as initial max
        return dfs(root, root.val)

    # Time & Space Complexity:
    # Time Complexity: O(n) where n is the number of nodes - we visit each node exactly once
    # Space Complexity: O(h) where h is the height of the tree - for the recursion stack (or explicit stack in iterative solution)

    # Similar Problems to Practice:
    # LeetCode 98: Validate Binary Search Tree (uses bounds propagation)
    # LeetCode 124: Binary Tree Maximum Path Sum
    # LeetCode 543: Diameter of Binary Tree

    # Common Tree Problems with This Pattern:
    # Similar Dual-Pattern Problems:
    # Path Sum: Check condition (preorder) + combine boolean results (postorder)
    # Tree Validation: Pass bounds down (preorder) + combine validity up (postorder)
    # Diameter of Tree: Pass depth info down + combine max diameter up

    # Pure Preorder Examples:
    # Tree serialization
    # Printing tree structure
    # Copying tree structure

    # Pure Postorder Examples:
    # Tree height calculation
    # Tree deletion
    # Bottom-up dynamic programming on trees

    # This dual pattern is very common in tree problems where you need to:
    # Pass context down (preorder)
    # Aggregate results up (postorder)


# @lc code=end


#
# @lcpr case=start
# [3,1,4,3,null,1,5]\n
# @lcpr case=end

# @lcpr case=start
# [3,3,null,4,2]\n
# @lcpr case=end

# @lcpr case=start
# [1]\n
# @lcpr case=end

#
