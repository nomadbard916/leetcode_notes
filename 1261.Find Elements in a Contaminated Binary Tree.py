#
# @lc app=leetcode id=1261 lang=python3
# @lcpr version=30201
#
# [1261] Find Elements in a Contaminated Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class FindElements:
    #  it's beginning with empty __init__() and find()
    def __init__(self, root: Optional[TreeNode]):
        # use "set" for faster lookup O(1) than O(n) of list
        self.recovered_values = set()
        self._recover_tree(root, 0)

    def _recover_tree(self, node: Optional[TreeNode], value: int) -> None:
        """
        Recursively recover the tree values using DFS traversal.

        Args:
            node: Current tree node being processed
            value: The correct value this node should have
        """
        if not node:
            return

        node.val = value
        self.recovered_values.add(value)

        if node.left:
            self._recover_tree(node.left, 2 * value + 1)
        if node.right:
            self._recover_tree(node.right, 2 * value + 2)

    def find(self, target: int) -> bool:
        return target in self.recovered_values

    # Time & Space Complexity:
    # Initialization: O(n) time, O(n) space where n is the number of nodes
    # Find operation: O(1) time, O(1) space
    # Overall space: O(n) for storing the recovered values in the set


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
# @lc code=end
