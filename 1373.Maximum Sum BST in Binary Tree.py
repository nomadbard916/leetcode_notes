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
        # 1. are left and right child tree BST?
        # 2. the max node of left child tree and the min node of right child tree
        # 3. the sum of left and right child tree nodes
        # but writing pre-order traversal needs many helper functions,
        # even worse, they are with recursion, making unnecessary complexity O(n^2)
        # ! mentioning "child trees" => post order!

        def find_vals_max_min_sum(root):
            # base case
            if root is None:
                # see definition below for "res"
                return [1, float("inf"), float("-inf"), 0]

            # calculate left and right child tree recursively
            left_child_res = find_vals_max_min_sum(root.left)
            right_child_res = find_vals_max_min_sum(root.right)

            # * post order operations
            # search for return values by left and right
            # and update max_sum accordingly
            # for fields in res arr:
            # res[0] records whether the binary tree rooted at root is a BST; if it is 1, it means it is a BST, if 0, it means it is not a BST;
            # res[1] records the minimum value among all nodes in the binary tree rooted at root;
            # res[2] records the maximum value among all nodes in the binary tree rooted at root;
            # res[3] records the sum of all node values in the binary tree rooted at root.
            res = [0, 0, 0, 0]
            if (
                left_child_res[0] == 1
                and right_child_res[0] == 1
                and root.val > left_child_res[2]
                and root.val < right_child_res[1]
            ):
                # the binary tree with "root" as root node is a BST
                res[0] = 1
                # take the min value from left child tree, or force assign if it's leaf node
                res[1] = min(left_child_res[1], root.val)
                # take the max value from right child tree, or force assign if it's leaf node
                res[2] = max(right_child_res[2], root.val)
                # calculate the sum of all nodes with "root" as the root node to this BST
                res[3] = left_child_res[3] + right_child_res[3] + root.val
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
