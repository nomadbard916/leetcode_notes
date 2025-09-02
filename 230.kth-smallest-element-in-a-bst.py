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

        # ! sol2: recursive
        self.result = None
        self.count = 0

        def inorder(node: TreeNode):
            if not node:
                return

            # * traverse left subtree
            inorder(node.left)

            # * process current
            self.count += 1
            if self.count == k:
                self.result = node.val
                return

            # * traverse right subtree
            inorder(node.right)

        inorder(root)
        return self.result

        # Iterative/Recursive Early Stopping:

        # Time Complexity: O(H + k) where H is height of tree
        # Best case (balanced): O(log n + k)
        # Worst case (skewed): O(n + k) ≈ O(n)

        # Space Complexity: O(H) for stack space
        # Best case: O(log n)
        # Worst case: O(n)

        # !sol3: brute force:
        # traverse postorderly the tree and put elements into a list,
        # then fetch list[k-1]

        def inorder(node: TreeNode) -> list[int]:
            if not node:
                return []
            return inorder(node.left) + [node.val] + inorder(node.right)

        values = inorder(root)
        return values[k - 1]  # k is 1-indexed, list is 0-indexed

        # Time Complexity: O(n) - must visit all nodes
        # Space Complexity: O(n) - store all values

        # ! sol4: min heap
        # we just use min heap as it's conceptually simple, but it's less efficient than max heap,
        # as max heap can keep only k smallest elements seen so far.
        #  Advantage: Works with ANY data structure, not just BSTs
        import heapq

        min_heap = []

        def traverse(node: TreeNode) -> None:
            if not node:
                return
            heapq.heappush(min_heap, node.val)
            traverse(node.left)
            traverse(node.right)

        traverse(root)

        for _ in range(k - 1):
            heapq.heappop(min_heap)

        return heapq.heappop(min_heap)

        # complexities
        #  Time: O(n log n + k log n)
        #  Space: O(n)


# @lc code=end
