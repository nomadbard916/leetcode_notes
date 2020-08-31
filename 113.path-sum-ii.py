#
# @lc app=leetcode id=113 lang=python3
#
# [113] Path Sum II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        paths = []

        if root is None:
            return paths

        def DFS(root=root, current_sum=0, current_path=[]):
            if root is None:
                return

            # preorder
            updated_path = current_path + [root.val]
            updated_sum = current_sum + root.val

            # ending condition
            if root.left is None and root.right is None and updated_sum == sum:
                paths.append(updated_path)
                return

            if root.left:
                DFS(root.left, updated_sum, updated_path)
            if root.right:
                DFS(root.right, updated_sum, updated_path)

        DFS()

        return paths


# @lc code=end

