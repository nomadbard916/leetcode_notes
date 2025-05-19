#
# @lc app=leetcode id=1373 lang=python3
# @lcpr version=30104
#
# [1373] Maximum Sum BST in Binary Tree
#

# @lc code=start
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self) -> None:
        self.max_sum = 0

    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        # on current standpoint, we need to know:
        # 1. are left and right child tree BST
        # 2. the max node of left child tree and the min node of right child tree
        # 3. the sum of left and right child tree nodes
        # but writing pre-order traversal needs many helper functions,
        # even worse, they are with recursion, making unnecessary complexity O(n^2)
        # mentioning "child trees" => post order!

        def find_vals_max_min_sum(root):
            # base case
            if root is None:
                return [1, float("inf"), float("-inf"), 0]

            # calculate left and right child tree recursively
            left = find_vals_max_min_sum(root.left)
            right = find_vals_max_min_sum(root.right)

            # * post order operations
            # search for return values by left and right
            # and update max_sum accordingly
            res = [0, 0, 0, 0]
            if (
                left[0] == 1
                and right[0] == 1
                and root.val > left[2]
                and root.val < right[1]
            ):
                # the binary tree with "root" as root node is a BST
                res[0] = 1
                # for a leaf node, get the min value for itself to be the leaf
                res[1] = min(left[1], root.val)
                # for a leaf node, get the max value for itself to be the leaf
                res[2] = max(right[2], root.val)
                # calculate the sum of all nodes with "root" as the root node to this BST
                res[3] = left[3] + right[3] + root.val
                # update the global variable
                self.max_sum = max(self.max_sum, res[3])

            return res

        find_vals_max_min_sum(root)
        return self.max_sum


# @lc code=end


#
# @lcpr case=start
# [1,4,3,2,4,2,5,null,null,null,null,null,null,4,6]\n
# @lcpr case=end

# @lcpr case=start
# [4,3,null,1,2]\n
# @lcpr case=end

# @lcpr case=start
# [-4,-2,-5]\n
# @lcpr case=end

#
