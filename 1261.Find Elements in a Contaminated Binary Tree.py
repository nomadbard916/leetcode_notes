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
        self._DFS_recover_tree_values(root, 0)

    def _DFS_recover_tree_values(
        self, curr_node: Optional[TreeNode], correct_value: int
    ) -> None:
        if not curr_node:
            return

        # Set the correct value for current node
        curr_node.val = correct_value
        # use additional DS for lookup anytime after the tree is recovered,
        # so we don't need to do tree traversal when find()
        self.recovered_values.add(correct_value)

        if curr_node.left:
            next_node_value = 2 * correct_value + 1
            self._DFS_recover_tree_values(curr_node.left, next_node_value)
        if curr_node.right:
            next_node_value = 2 * correct_value + 2
            self._DFS_recover_tree_values(curr_node.right, next_node_value)

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
