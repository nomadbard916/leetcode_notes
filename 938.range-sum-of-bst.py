#
# @lc app=leetcode id=938 lang=python3
#
# [938] Range Sum of BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        global ans
        ans = 0

        def DFS(root=root):
            if not root:
                return

            if root.val >= L and root.val <= R:
                global ans
                ans += root.val

            DFS(root.left)
            DFS(root.right)

        DFS()

        return ans


# @lc code=end

