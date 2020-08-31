from collections import deque

#
# @lc app=leetcode id=114 lang=python3
#
# [114] Flatten Binary Tree to Linked List
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root is None:
            return root

        queue = deque()

        def DFS(root):
            if root is None:
                return
            queue.append(root)

            DFS(root.left)
            DFS(root.right)

        DFS(root)

        root = queue.popleft()

        while len(queue) > 0:
            if root.left:
                root.left = None
            root.right = queue.popleft()

            root = root.right


# @lc code=end

