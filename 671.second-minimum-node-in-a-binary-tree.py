#
# @lc app=leetcode id=671 lang=python3
#
# [671] Second Minimum Node In a Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        if not root:
            return -1

        container = set()

        def DFS(root):
            if not root:
                return

            container.add(root.val)

            DFS(root.left)
            DFS(root.right)

        DFS(root)

        sorted_list = sorted(list(set(container)))

        return sorted_list[1] if len(sorted_list) >= 2 else -1


# @lc code=end

