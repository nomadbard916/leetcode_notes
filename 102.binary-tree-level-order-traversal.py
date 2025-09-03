#
# @lc app=leetcode id=102 lang=python3
#
# [102] Binary Tree Level Order Traversal
#

# @lc code=start
from collections import deque
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        ans = []
        # sanity check
        if not root:
            return ans

        q = deque([root])

        while q:
            curr_lv_nodes = []
            curr_q_len = len(q)

            # check each node in this level
            for _ in range(curr_q_len):
                # current level operation
                current_node = q.popleft()
                curr_lv_nodes.append(current_node.val)

                # check next level and put nodes into queue
                if current_node.left:
                    q.append(current_node.left)
                if current_node.right:
                    q.append(current_node.right)

            if len(curr_lv_nodes) > 0:
                ans.append(curr_lv_nodes)

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
