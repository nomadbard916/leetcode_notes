#
# @lc app=leetcode id=1448 lang=python3
# @lcpr version=30201
#
# [1448] Count Good Nodes in Binary Tree
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
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node: Optional[TreeNode], max_val: int) -> int:
            #  * base case: if node is None, no good nodes
            if not node:
                return 0

            good_count = 0
            # Check if current node is good
            # * node is good if its value >= max value in path from root
            if node.val >= max_val:
                good_count = 1

            # Update max_val for children - it's the maximum of current max_val and current node's value
            new_max = max(max_val, node.val)

            # * post order logic
            # Recursively count good nodes in left and right subtrees
            good_count += dfs(node.left, new_max)
            good_count += dfs(node.right, new_max)

            return good_count

        # Start DFS from root with root's value as initial max
        return dfs(root, root.val)


# @lc code=end


#
# @lcpr case=start
# [3,1,4,3,null,1,5]\n
# @lcpr case=end

# @lcpr case=start
# [3,3,null,4,2]\n
# @lcpr case=end

# @lcpr case=start
# [1]\n
# @lcpr case=end

#
