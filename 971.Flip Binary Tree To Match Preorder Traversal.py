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
        # * it is asking you to iterate through 2 DS at once, see # 1367

        #  * this is fundamentally a "traversal order selection" algorithm disguised as a "tree flipping" algorithm.
        # The "flipping" is conceptual - we're really just choosing which child to visit first at each step!

        # * What We're NOT Doing vs What We ARE Doing
        # NOT Actually Flipping:
        # - We don't modify the tree structure
        # - We don't physically swap left and right pointers
        # - The tree remains unchanged throughout the algorithm

        # What We ARE Actually Doing:
        # - Dynamically choosing traversal order based on the voyage requirements
        # - Recording which nodes would need to be flipped if we were to physically modify the tree
        # - Simulating the result of what the preorder traversal would be if flips were applied

        # Instead of:
        # 1. Try all possible combinations of flips → exponential complexity
        # 2. Actually flip nodes and check → requires tree modification

        # We do:
        # 1. Greedily decide traversal order based on immediate needs
        # 2. Simulate the result of flips without actual modifications
        # 3. Validate in linear time

        # Store nodes that we flip
        flipped = []
        # TODO: modify this to parameter passing, as functional style has more pros.
        # Track current position in voyage
        self.index = 0

        def dfs(node: Optional[TreeNode]) -> bool:
            if not node:
                return True

            if self.index >= len(voyage):
                return False

            # Check if current node matches expected value in voyage
            if node.val != voyage[self.index]:
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

            # * Both children exist - check if we need to flip
            curr_voyage_val = voyage[self.index]

            # Left child matches next expected value
            if node.left.val == curr_voyage_val:
                # No flip needed because the natural traversal order already matches what we want.
                return dfs(node.left) and dfs(node.right)

            # Right child matches next expected value
            if node.right.val == curr_voyage_val:
                # The flip is needed because preorder always visits left subtree before right subtree.
                flipped.append(node.val)
                # traverse right first as it's the new left after flipped in pre-order traversal
                return dfs(node.right) and dfs(node.left)

            # Neither child matches - impossible to match voyage
            return False

        if dfs(root):
            return flipped

        return [-1]

        # Time and Space Complexity

        # Time Complexity: O(n) where n is the number of nodes in the tree
        # - We visit each node exactly once
        # - Each node operation is O(1)

        # Space Complexity: O(h + f) where h is the height of the tree and f is the number of flips
        # - O(h) for the recursion stack (worst case O(n) for skewed tree)
        # - O(f) for storing the flipped nodes list (worst case O(n))
        # - Overall: O(n) in the worst case


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
