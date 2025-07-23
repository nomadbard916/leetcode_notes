#
# @lc app=leetcode id=654 lang=python3
# @lcpr version=30201
#
# [654] Maximum Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
from typing import List, Optional

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None

        max_val = max(nums)
        max_idx = nums.index(max_val)

        root = TreeNode(max_val)

        root.left = self.constructMaximumBinaryTree(nums[:max_idx])
        root.right = self.constructMaximumBinaryTree(nums[max_idx + 1 :])

        return root


# @lc code=end


#
# @lcpr case=start
# [3,2,1,6,0,5]\n
# @lcpr case=end

# @lcpr case=start
# [3,2,1]\n
# @lcpr case=end

#
