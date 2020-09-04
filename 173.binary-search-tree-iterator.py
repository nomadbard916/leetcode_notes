#
# @lc app=leetcode id=173 lang=python3
#
# [173] Binary Search Tree Iterator
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:
    def __init__(self, root: TreeNode):
        self.sorted_nodes = []
        # initially just outside of list, acting like dummy
        self.index = -1
        self._inorder(root)

    def next(self) -> int:
        """
        @return the next smallest number
        """
        self.index += 1

        return self.sorted_nodes[self.index]

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """

        return self.index + 1 < len(self.sorted_nodes)

    def _inorder(self, root):
        if root is None:
            return

        self._inorder(root.left)
        self.sorted_nodes.append(root.val)
        self._inorder(root.right)


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
# @lc code=end

