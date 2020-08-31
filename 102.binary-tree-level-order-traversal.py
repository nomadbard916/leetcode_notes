#
# @lc app=leetcode id=102 lang=python3
#
# [102] Binary Tree Level Order Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        ans = []
        q = deque([root])

        # sanity check
        if not root:
            return ans

        while q:
            current_level = []
            length = len(q)

            # check each node in this level
            for i in range(length):
                # current level operation
                current_node = q.popleft()
                current_level.append(current_node.val)

                # check next level and put nodes into queue
                if current_node.left:
                    q.append(current_node.left)
                if current_node.right:
                    q.append(current_node.right)

            if len(current_level) > 0:
                ans.append(current_level)

        return ans

        # sol2: DFS
        # if root is None:
        #     return root

        # ans = []

        # def DFS(root=root, current_depth=1):
        #     if root is None:
        #         return root

        #     previous_depth = len(ans)

        #     if current_depth > previous_depth:
        #         ans.append([])

        #     ans[current_depth - 1].append(root.val)

        #     next_depth = current_depth + 1
        #     DFS(root.left, next_depth)
        #     DFS(root.right, next_depth)

        # DFS()

        # return ans


# @lc code=end

