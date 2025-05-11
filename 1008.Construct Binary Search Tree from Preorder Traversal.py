#
# @lc app=leetcode id=1008 lang=python3
# @lcpr version=30104
#
# [1008] Construct Binary Search Tree from Preorder Traversal
#

# @lc code=start
from typing import List, Optional


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        # sol1: DFS with stack
        # First item in preorder list is the root to be considered.
        root = TreeNode(preorder[0])
        stack = [root]
        # For next item in preorder list, there are 2 cases to consider:
        for value in preorder[1:]:
            # If value is less than last item in stack, it is the left child of last item.
            if value < stack[-1].val:
                stack[-1].left = TreeNode(value)
                stack.append(stack[-1].left)
            else:
                # If value is greater than last item in stack, pop it.
                while stack and stack[-1].val < value:
                    last = stack.pop()
                # The last popped item will be the parent and the item will be the right child of the parent.
                last.right = TreeNode(value)
                stack.append(last.right)
        return root

        # sol2: problem decomposition,
        if not preorder:
            return None

        # First element in preorder is the root
        root_val = preorder[0]
        root = TreeNode(root_val)

        # Find the index where values become greater than root_val
        # This is where the right subtree starts
        i = 1
        while i < len(preorder) and preorder[i] < root_val:
            i += 1

        # Recursively build left and right subtrees
        root.left = self.bstFromPreorder(preorder[1:i])
        root.right = self.bstFromPreorder(preorder[i:])

        return root


# @lc code=end


#
# @lcpr case=start
# [8,5,1,7,10,12]\n
# @lcpr case=end

# @lcpr case=start
# [1,3]\n
# @lcpr case=end

#
