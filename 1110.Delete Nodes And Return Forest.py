#
# @lc app=leetcode id=1110 lang=python3
# @lcpr version=30201
#
# [1110] Delete Nodes And Return Forest
#

# @lc code=start
# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def delNodes(
        self, root: Optional[TreeNode], to_delete: List[int]
    ) -> List[TreeNode]:
        # convert list to set for O(1) lookup
        delete_set = set(to_delete)
        result = []

        def dfs(node: Optional[TreeNode], is_root: bool) -> Optional[TreeNode]:
            if not node:
                return
            should_delete = node.val in delete_set

            if is_root and not should_delete:
                result.append(node)

            node.left = dfs(node.left, should_delete)
            node.right = dfs(node.right, should_delete)

            if should_delete:
                return None

            return node

        dfs(root, True)

        return result


# @lc code=end


#
# @lcpr case=start
# [1,2,3,4,5,6,7]\n[3,5]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,4,null,3]\n[3]\n
# @lcpr case=end

#
