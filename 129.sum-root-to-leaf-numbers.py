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
        if root is None:
            return 0

        list_container = []

        def DFS(current_path: list, root=root):
            updated_path = current_path + [str(root.val)]

            if root.left is None and root.right is None:
                list_container.append(updated_path)
                return

            if root.left:
                DFS(updated_path, root.left)

            if root.right:
                DFS(updated_path, root.right)

        current_path = []
        DFS(current_path)

        int_container = list(map(lambda x: int("".join(x)), list_container))

        return sum(int_container)


# @lc code=end
