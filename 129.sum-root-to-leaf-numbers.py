#
# @lc app=leetcode id=129 lang=python3
#
# [129] Sum Root to Leaf Numbers
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        list_container = []

        def DFS(root=root, current_path=[]):
            if root.left is None and root.right is None:
                list_container.append(current_path)
                return

            # preorder
            updated_path = current_path + [root.val]
            DFS(root.left, updated_path)
            DFS(root.right, updated_path)

        DFS()

        value_container = []
        for num_list in list_container:
            # each item in num_list is int here
            value_container.append(int("".join(num_list)))

        return sum(value_container)


# @lc code=end

