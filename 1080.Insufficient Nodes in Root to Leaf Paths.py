#
# @lc app=leetcode id=1080 lang=python3
# @lcpr version=30201
#
# [1080] Insufficient Nodes in Root to Leaf Paths
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
    def sufficientSubset(
        self, root: Optional[TreeNode], limit: int
    ) -> Optional[TreeNode]:
        # ! sol1:
        # Core Insight: We need to work bottom-up (post-order traversal)
        # because we can only determine if a node should be removed after we know about its children's sufficiency.
        # briefly, the whole process is about: it about traversing all the way to leaf,
        # determine if we want to remove it, go one layer up back and finally all the way to root
        # Step-by-Step Mental Model:
        # Think of it like bottom-up decision making:

        # Go to leaves first: "I'm a leaf, my path sum is X, should I stay?" ✓
        # Go up one level: "My children decided their fate, now I can decide mine" ✓
        # Keep going up: Each parent makes decisions based on children's decisions ✓
        # Reach root: Finally decide about the root based on its children ✓

        # Think of a company layoff scenario:
        # Wrong approach: CEO decides who to fire before knowing what each department contributes
        # Right approach: Evaluate each team's contribution bottom-up, then decide which managers are still needed based on their remaining teams

        # * Base case: if in emptiness, just return
        if not root:
            return
        # * If this is a leaf node, check if current path sum meets the limit
        if not root.left and not root.right:
            # If leaf value is >= limit, keep it; otherwise remove it
            return root if root.val >= limit else None

        # For internal nodes, recursively process children
        # Update limit by subtracting current node's value
        # that is, update the limit that's applicable for this subtree
        new_limit = limit - root.val

        # Recursively process left and right subtrees,
        # so post-order code can know about children info
        root.left = self.sufficientSubset(root.left, new_limit)
        root.right = self.sufficientSubset(root.right, new_limit)

        # * post order logic: My children decided their fate, now I can decide mine
        # After processing children and going back to this parent node,
        # check if current node should be kept if at least one child remains
        # meaning at least one path through this node is sufficient
        if root.left or root.right:
            return root
        else:
            return None

        # !sol2: explicit path sum tracking with DFS helper
        def dfs(node: TreeNode, current_sum: int) -> TreeNode:
            if not node:
                return
            current_sum += node.val

            # If leaf node, check if path sum is sufficient
            if not node.left and not node.right:
                return node if current_sum >= limit else None

            # Process children
            node.left = dfs(node.left, current_sum)
            node.right = dfs(node.right, current_sum)

            # Keep node if at least one child remains
            return node if (node.left or node.right) else None

        return dfs(root, 0)


# @lc code=end


#
# @lcpr case=start
# [1,2,3,4,-99,-99,7,8,9,-99,-99,12,13,-99,14]\n1\n
# @lcpr case=end

# @lcpr case=start
# [5,4,8,11,null,17,4,7,1,null,null,5,3]\n22\n
# @lcpr case=end

# @lcpr case=start
# [1,2,-3,-5,null,4,null]\n-1\n
# @lcpr case=end

#
