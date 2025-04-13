#
# @lc app=leetcode id=988 lang=python3
# @lcpr version=30104
#
# [988] Smallest String Starting From Leaf
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    path = ""
    res = None

    def traverse(self, root):
        if root is None:
            return

        # when on the leaf node, compare with the smallest order path
        # remember to reverse sequence to fit the answer
        if root.left is None and root.right is None:
            self.path = chr(ord("a") + root.val) + self.path

            s = self.path
            # update res
            if self.res is None or self.res > s:
                self.res = s

            self.path = self.path[1:]
            return

        # pre-order
        self.path = chr(ord("a") + root.val) + self.path

        self.traverse(root.left)
        self.traverse(root.right)

        # post order
        self.path = self.path[1:]

    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        self.traverse(root)
        return self.res


# @lc code=end


#
# @lcpr case=start
# [0,1,2,3,4,3,4]\n
# @lcpr case=end

# @lcpr case=start
# [25,1,3,1,3,0,2]\n
# @lcpr case=end

# @lcpr case=start
# [2,2,1,null,1,0,null,0]\n
# @lcpr case=end

#
