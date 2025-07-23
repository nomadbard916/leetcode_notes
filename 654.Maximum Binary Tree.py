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
        # ! sol 1: Recursive Divide and Conquer
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

        # ! sol2: Optimized Stack Solution (Advanced)
        # Key Insights:
        # 1. Process numbers left to right
        # 2. Maintain stack of nodes in decreasing order
        # 3. When we find a larger number, it becomes the parent of smaller numbers we pop

        # How it works:
        # - Stack maintains potential parents in decreasing order
        # - When current number > stack top: current becomes parent of popped elements
        # - When current number < stack top: current becomes right child of stack top
        stack = []

        for num in nums:
            node = TreeNode(num)

            # Pop smaller elements and make the last popped element
            # the left child of current node
            last_popped = None
            while stack and stack[-1].val < nums:
                last_popped = stack.pop()

                if last_popped:
                    node.left = last_popped

                # If stack is not empty, current node becomes right child
                # of the top element in stack
                if stack:
                    stack[-1].right = node

                stack.append(node)

        # The bottom element of stack is the root
        if stack:
            return stack[0]

        return None


# @lc code=end


#
# @lcpr case=start
# [3,2,1,6,0,5]\n
# @lcpr case=end

# @lcpr case=start
# [3,2,1]\n
# @lcpr case=end

#
