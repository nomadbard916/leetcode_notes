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
        # ! sol1: find the shortest path from start to dest, both starting  root
        # Core Insight: The shortest path between any two nodes in a tree must pass through their Lowest Common Ancestor (LCA). So the path will be:
        # - Go UP from start node to LCA
        # - Go DOWN from LCA to destination node
        def find_path(node: Optional[TreeNode], target: int, path: list[str]) -> bool:
            if not node:
                return False

            if node.val == target:
                return True

            # Try going left
            path.append("L")
            if find_path(node.left, target, path):
                return True
            path.pop()  # Backtrack

            # Try going right
            path.append("R")
            if find_path(node.right, target, path):
                return True
            path.pop()  # Backtrack

            # The current node is NOT the target node (node.val != target)
            # The target was NOT found in the left subtree
            # The target was NOT found in the right subtree
            # If we removed the return False, the function would implicitly return None in Python.
            return False

        # Find paths from root to both nodes
        start_path: list[str] = []
        find_path(root, startValue, start_path)
        dest_path: list[str] = []
        find_path(root, destValue, dest_path)

        # Find LCA, the point where paths diverge, by comparing paths to remove common prefix (path to LCA)
        i = 0
        while (
            i < len(start_path) and i < len(dest_path) and start_path[i] == dest_path[i]
        ):
            i += 1

        # Build result:
        # - 'U' for each step from start to LCA
        # - Remaining path from LCA to destination
        result = "U" * (len(start_path) - i) + "".join(dest_path[i:])

        return result

        # Time and Space Complexity
        # Time Complexity: O(n) where n is the number of nodes
        # We visit each node at most once during path finding
        # Path comparison takes O(h) where h is height

        # Space Complexity: O(h) where h is the height of the tree
        # Recursion stack depth is O(h)
        # Path storage is O(h)

        # ! sol2: find LCA directly and start from there
        # the LCA approach may look more intuitive but is NOT faster than the first approach - they have the same time complexity,
        # and LCA makes up to  tree traversals and therefore extra recursion stack,
        # while the first approach is actually more efficient in practice with 2 tree traversals and has early termination.
        def find_lca(node: TreeNode, p: int, q: int) -> TreeNode:
            if not node:
                return None

            if node.val == p or node.val == q:
                return node

            left = find_lca(node.left, p, q)
            right = find_lca(node.right, p, q)

            # This means both p and q were found in different subtrees, so root is their LCA.
            if left and right:
                return node

            # If one is not None, propagate that node up the recursion.
            return left or right

        def find_path_from_node(node: TreeNode, target: int, path: list[str]) -> bool:
            if not node:
                return False
            if node.val == target:
                return True

            path.append("L")
            if find_path_from_node(node.left, target, path):
                return True
            path.pop()

            path.append("R")
            if find_path_from_node(node.right, target, path):
                return True
            path.pop()

            return False

        lca = find_lca(root, startValue, destValue)

        start_path: list[str] = []
        find_path_from_node(lca, startValue, start_path)
        dest_path: list[str] = []
        find_path_from_node(lca, startValue, dest_path)

        return "U" * len(start_path) + "".join(dest_path)


# @lc code=end


#
# @lcpr case=start
# [5,1,2,3,null,6,4]\n3\n6\n
# @lcpr case=end

# @lcpr case=start
# [2,1]\n2\n1\n
# @lcpr case=end

#
