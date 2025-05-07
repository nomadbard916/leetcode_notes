#
# @lc app=leetcode id=437 lang=python3
# @lcpr version=30104
#
# [437] Path Sum III
#

# @lc code=start
# Definition for a binary tree node.
from collections import defaultdict
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        # of course we can do brute force, but
        # time complexity O(n square), space complexity O(h)

        # prefix sums encountered in current path
        prefix_sums_dict = defaultdict(int)
        prefix_sums_dict[0] = 1

        def dfs(root, curr_sum):
            count = 0
            if root is None:
                return count

            curr_sum += root.val
            count = prefix_sums_dict[curr_sum - targetSum]

            prefix_sums_dict[curr_sum] += 1
            count += dfs(root.left, curr_sum)
            count += dfs(root.right, curr_sum)

            prefix_sums_dict[curr_sum] -= 1

            return count

        return dfs(root, 0)


# @lc code=end


#
# @lcpr case=start
# [10,5,-3,3,2,null,11,3,-2,null,1]\n8\n
# @lcpr case=end

# @lcpr case=start
# [5,4,8,11,null,13,4,7,2,null,null,5,1]\n22\n
# @lcpr case=end

#
