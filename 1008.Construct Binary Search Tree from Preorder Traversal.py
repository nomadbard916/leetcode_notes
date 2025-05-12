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
        if not preorder:
            return None
        # First item in preorder list is the root to be considered.
        root = TreeNode(preorder[0])
        stack = [root]
        # For next item in preorder list, there are 2 cases to consider:
        for value in preorder[1:]:
            node = TreeNode(value)

            # case 1: If current value is less than the top item in stack,
            # it is the left child of top item.
            if value < stack[-1].val:
                stack[-1].left = node
            else:
                parent: Optional[TreeNode] = None
                # case 2: If value is greater than top item in stack,
                # pop nodes until we find the right parent
                while stack and stack[-1].val < value:
                    parent = stack.pop()
                # The last popped item will be the parent and the item will be the right child of the parent.
                parent.right = node

            # Always push the new node onto the stack
            stack.append(node)
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
