#
# @lc app=leetcode id=230 lang=python3
#
# [230] Kth Smallest Element in a BST
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    ans: int = 0
    count: int = 0

    def kthSmallest(self, root: TreeNode, k: int) -> int:
        # ! sol1: iterative in-order traversal, most efficient
        stack = []
        current = root
        count = 0

        while stack or current:
            # go to the leftmost node
            while current:
                stack.append(current)
                current = current.left

            #  process the current node
            current = stack.pop()
            count += 1

            # if we've found the kth element, return it
            if count == k:
                return current.val

            # move to right subtree
            current = current.right

        # Should never reach here if k is valid
        return -1

        # Iterative/Recursive Early Stopping:

        # Time Complexity: O(H + k) where H is height of tree
        # Best case (balanced): O(log n + k)
        # Worst case (skewed): O(n + k) ≈ O(n)

        # Space Complexity: O(H) for stack space
        # Best case: O(log n)
        # Worst case: O(n)

        # !sol: brute force:
        # traverse postorderly the tree and put elements into a t_list,
        # then fetch t_list[-k]

        # in-order traversal for BST, and record k ordering in the process
        # when to update k value?

        def DFS(root):
            if root is None:
                return

            DFS(root.left)

            # in BST, as left child node must be smaller than parent rood node,
            # the traversal count should be recorded here
            self.count += 1
            if self.count == k:
                self.ans = root.val

            DFS(root.right)

        DFS(root)

        return self.ans

        # Time Complexity: O(n) - must visit all nodes
        # Space Complexity: O(n) - store all values


# @lc code=end
