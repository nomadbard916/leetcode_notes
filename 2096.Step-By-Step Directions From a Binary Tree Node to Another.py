#
# @lc app=leetcode id=2096 lang=python3
# @lcpr version=30201
#
# [2096] Step-By-Step Directions From a Binary Tree Node to Another
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
    def getDirections(
        self, root: Optional[TreeNode], startValue: int, destValue: int
    ) -> str:
        # Core Insight: The shortest path between any two nodes in a tree must pass through their Lowest Common Ancestor (LCA). So the path will be:
        # - Go UP from start node to LCA
        # - Go DOWN from LCA to destination node
        def find_path(node: Optional[TreeNode], target: int, path: list[str]) -> bool:
            if not node:
                return False

            if node.val == target:
                return True

            path.append("L")
            if find_path(node.left, target, path):
                return True
            path.pop()

            path.append("R")
            if find_path(node.right, target, path):
                return True
            path.pop()

            return False

        start_path: list[str] = []
        dest_path: list[str] = []

        find_path(root, startValue, start_path)
        find_path(root, destValue, dest_path)

        i = 0
        while (
            i < len(start_path) and i < len(dest_path) and start_path[i] == dest_path[i]
        ):
            i += 1

        result = "U" * (len(start_path) - i) + "".join(dest_path[i:])

        return result

        # Time and Space Complexity
        # Time Complexity: O(n) where n is the number of nodes
        # We visit each node at most once during path finding
        # Path comparison takes O(h) where h is height

        # Space Complexity: O(h) where h is the height of the tree
        # Recursion stack depth is O(h)
        # Path storage is O(h)


# @lc code=end


#
# @lcpr case=start
# [5,1,2,3,null,6,4]\n3\n6\n
# @lcpr case=end

# @lcpr case=start
# [2,1]\n2\n1\n
# @lcpr case=end

#
