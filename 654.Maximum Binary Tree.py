#
# @lc app=leetcode id=654 lang=python3
# @lcpr version=30201
#
# [654] Maximum Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
from typing import List, Optional

# ! do not uncomment this, or test will fail
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None

        # Find the maximum value and its index
        max_val = max(nums)
        max_idx = nums.index(max_val)

        root = TreeNode(max_val)

        # take all the left subarray to max element to build left child tree
        root.left = self.constructMaximumBinaryTree(nums[:max_idx])
        # take all the left subarray to max element to build right child tree
        root.right = self.constructMaximumBinaryTree(nums[max_idx + 1 :])

        return root

        # Time Complexity: O(n²) in worst case
        # Finding max: O(n)
        # Array slicing: O(n)
        # Done for each node: O(n) nodes
        # Worst case (sorted array): O(n²)

        # Space Complexity: O(n)
        # Recursion depth: O(n) in worst case
        # Array slicing creates new arrays: O(n) space


# @lc code=end


#
# @lcpr case=start
# [3,2,1,6,0,5]\n
# @lcpr case=end

# @lcpr case=start
# [3,2,1]\n
# @lcpr case=end

#
