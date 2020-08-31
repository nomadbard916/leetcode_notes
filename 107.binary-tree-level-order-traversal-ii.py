#
# @lc app=leetcode id=107 lang=python3
#
# [107] Binary Tree Level Order Traversal II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        # see # 102 for implementation using queue
        # just traverse top-down as in 102 and reverse is also feasible

        if not root:
            return root

        ans = []

        def DFS(root=root, current_depth=1):
            if root is None:
                return

            previous_depth = len(ans)
            # already go down to next layer
            if current_depth > previous_depth:
                ans.insert(0, [])

            # preorder
            # directly appoint the depth level to append to
            ans[-(current_depth)].append(root.val)

            next_depth = current_depth + 1

            DFS(root.left, next_depth)
            DFS(root.right, next_depth)

        DFS()

        return ans


# @lc code=end

