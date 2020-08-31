#
# @lc app=leetcode id=199 lang=python3
#
# [199] Binary Tree Right Side View
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        # see only right nodes
        if root is None:
            return root

        ans = []

        def DFS(root=root, current_level=0):
            if root is None:
                return

            # preorder, but as we only want to see right nodes...
            # there should be only one rightmost node shown in ans
            if current_level == len(ans):
                ans.append(root.val)

            DFS(root.right, current_level + 1)
            DFS(root.left, current_level + 1)

        DFS()

        return ans


# @lc code=end

