#
# @lc app=leetcode id=112 lang=python3
#
# [112] Path Sum
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        def DFS(root=root, path_sum=0):
            # ending condition: out of bound and there's still no matching sum
            if root is None:
                return False

            path_sum += root.val

            # when on leaf node and match is found
            if path_sum == sum and root.left is None and root.right is None:
                return True

            return DFS(root.left, path_sum) or DFS(root.right, path_sum)

        return DFS()


# @lc code=end

