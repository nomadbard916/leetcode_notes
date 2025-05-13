#
# @lc app=leetcode id=652 lang=python3
# @lcpr version=30104
#
# [652] Find Duplicate Subtrees
#

# @lc code=start
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findDuplicateSubtrees(
        self, root: Optional[TreeNode]
    ) -> List[Optional[TreeNode]]:
        res = []
        hmap = {}

        def recurse(root):
            if root is None:
                return "#"

            left_subtree = recurse(root.left)
            right_subtree = recurse(root.right)
            subtree = left_subtree + "," + right_subtree + "," + str(root.val)

            freq = hmap.get(subtree, 0)
            if freq == 1:
                res.append(root)

            hmap[subtree] = freq + 1

            return subtree

        recurse(root)
        return res


# @lc code=end


#
# @lcpr case=start
# [1,2,3,4,null,2,4,null,null,4]\n
# @lcpr case=end

# @lcpr case=start
# [2,1,1]\n
# @lcpr case=end

# @lcpr case=start
# [2,2,2,3,null,3,null]\n
# @lcpr case=end

#
