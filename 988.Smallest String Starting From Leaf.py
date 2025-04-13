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
        # the pre-order operation is used to construct the path as the traversal goes deeper, and the post-order operation is used to backtrack and maintain the correct path state. This combination is necessary for the specific problem of finding the smallest string from leaf to root.
        if root is None:
            return

        if root.left is None and root.right is None:
            self.path = chr(ord("a") + root.val) + self.path

            s = self.path
            # update res
            if self.res is None or self.res > s:
                self.res = s

            # Remove current node's character from the path
            self.path = self.path[1:]
            return

        # Pre-order: Add current node's character to the path
        self.path = chr(ord("a") + root.val) + self.path

        self.traverse(root.left)
        self.traverse(root.right)

        # Post-order: Remove current node's character from the path
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
