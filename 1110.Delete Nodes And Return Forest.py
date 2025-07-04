#
# @lc app=leetcode id=1110 lang=python3
# @lcpr version=30201
#
# [1110] Delete Nodes And Return Forest
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
    def delNodes(
        self, root: Optional[TreeNode], to_delete: List[int]
    ) -> List[TreeNode]:
        # ! Core Algorithm: DFS with State Tracking
        # The key insight is to use Depth-First Search (DFS) while tracking whether
        # each node could potentially be a root of a tree in the final result.

        # convert to set for O(1) lookup instead of O(n) list search
        delete_set = set(to_delete)

        result = []

        # * DFS with Root Tracking: Each recursive call tracks if the current node is a potential root
        def dfs(node: Optional[TreeNode], can_be_root: bool) -> Optional[TreeNode]:
            if not node:
                return

            should_delete = node.val in delete_set

            # * This pre-order part is for result collection only, not for tree modification.
            # The tree structure modification happens AFTER we decide what to append.
            # When we append a node, we're appending the reference to this node ,
            # but the tree structure will be modified by the subsequent recursive calls.
            if can_be_root and not should_delete:
                result.append(node)

            # *Recursively process children
            # If current node is deleted, its children become potential roots
            # This is why we pass the state "should_delete" of parent
            # as the "can_be_root" state for children
            node.left = dfs(node.left, should_delete)
            node.right = dfs(node.right, should_delete)

            # * post order logic to delete or just keep the node
            return None if should_delete else node  # keep

        dfs(root, True)

        return result

        # Complexity Analysis:
        # Time Complexity: O(n)

        # Visit each node exactly once in DFS
        # Set lookup for deletion check is O(1)
        # Overall: O(n) where n is number of nodes

        # Space Complexity: O(n + h)

        # O(n) for the delete_set
        # O(h) for recursion stack where h is tree height
        # In worst case (skewed tree): O(n)
        # In best case (balanced tree): O(log n)


# @lc code=end


#
# @lcpr case=start
# [1,2,3,4,5,6,7]\n[3,5]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,4,null,3]\n[3]\n
# @lcpr case=end

#
