#
# @lc app=leetcode id=450 lang=python3
# @lcpr version=30104
#
# [450] Delete Node in a BST
#

# @lc code=start
# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getMin(self, node: TreeNode) -> TreeNode:
        # for BST, ths left-most child node is the smallest node
        while node.left is not None:
            node = node.left
        return node

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # ! sol1: connecting nodes and replace
        if root is None:
            return None

        # * search phase first
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:  # found: root.val == key
            # * start deleting, but cannot break the BST. 3 possibilities:
            # 1: it's the leaf node, just remove it;
            # in below code it's covered by just returning None
            # 2: only one child node, then just let the child substitute itself
            # this block is also used when deleting minNode
            if root.left is None:
                return root.right
            if root.right is None:
                return root.left
            # 3: the root has two children nodes.
            # in order not to break BST when substituting the root with child node
            # and keep the connection continuous:
            # find the biggest node in left sub tree,
            # or the smallest child node in right sub tree.
            minNode = self.getMin(root.right)
            # delete the minNode in right tree
            root.right = self.deleteNode(root.right, minNode.val)
            # take the minNode in right sub tree to subsitute the root
            minNode.left = root.left
            minNode.right = root.right
            root = minNode
        return root
        # Time Complexity: O(h) where h is the height of the tree. In the worst case, we might need to traverse from the root to the deepest leaf node (height of the tree). For a balanced BST, this would be O(log n), but in the worst case (skewed tree), it could be O(n).
        # Space Complexity: O(h) due to the recursion stack. Again, in the worst case, this could be O(n) for a skewed tree.

        # ! sol2: replace value only
        # 1. First find the node that we need to delete.
        # 2. After it’s found, think about ways to keep the tree BST after deleting the node.
        # - If there’s no left or right subtree, we found the leaf. Delete this node without any further traversing.
        # - If it’s not a leaf node, what node we can use from the subtree that can replace the delete node and still maintain the BST property?
        # We can either replace the delete node with the minimum from the right subtree (if right exists)
        # or we can replace the delete node with the maximum from the left subtree (if left exists).
        def get_min_in_right_tree(self, root: TreeNode) -> int:
            root = root.right
            while root.left:
                root = root.left
            return root.val

        def get_max_in_left_tree(self, root: TreeNode) -> int:
            root = root.left
            while root.right:
                root = root.right
            return root.val

        if not root:
            return None

        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            if not root.left and not root.right:
                root = None
            # it looks for right tree first, essentially it's the same as sol1
            elif root.right:
                # replace the value of root by min in right
                root.val = get_min_in_right_tree(root)
                # reconnecting this "root" to the root of right tree
                root.right = self.deleteNode(root.right, root.val)
            else:
                root.val = get_max_in_left_tree(root)
                root.left = self.deleteNode(root.left, root.val)
        return root

        # ! sol3: iterative
        if not root:
            return None

        # Handle the case where the root is the node to delete
        if root.val == key:
            if not root.left:
                return root.right
            if not root.right:
                return root.left

            # Find successor (smallest node in right subtree)
            successor = root.right
            while successor.left:
                successor = successor.left

            successor.left = root.left
            return root.right

        parent = None
        curr = root

        # Find the node to delete and its parent
        while curr and curr.val != key:
            parent = curr
            if key < curr.val:
                curr = curr.left
            else:
                curr = curr.right

        if not curr:  # Node not found
            return root

        # Case 1 & 2: Node has 0 or 1 child
        if not curr.left:
            if parent.left == curr:
                parent.left = curr.right
            else:
                parent.right = curr.right
        elif not curr.right:
            if parent.left == curr:
                parent.left = curr.left
            else:
                parent.right = curr.left
        else:  # Case 3: Node has 2 children
            successor_parent = curr
            successor = curr.right

            # Find the leftmost node in the right subtree
            while successor.left:
                successor_parent = successor
                successor = successor.left

            # Replace the node value with successor's value
            curr.val = successor.val

            # Delete the successor
            if successor_parent.left == successor:
                successor_parent.left = successor.right
            else:
                successor_parent.right = successor.right

        return root


# @lc code=end


#
# @lcpr case=start
# [5,3,6,2,4,null,7]\n3\n
# @lcpr case=end

# @lcpr case=start
# [5,3,6,2,4,null,7]\n0\n
# @lcpr case=end

# @lcpr case=start
# []\n0\n
# @lcpr case=end

#
