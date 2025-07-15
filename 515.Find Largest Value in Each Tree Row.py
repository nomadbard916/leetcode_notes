#
# @lc app=leetcode id=515 lang=python3
# @lcpr version=30201
#
# [515] Find Largest Value in Each Tree Row
#

# @lc code=start
# Definition for a binary tree node.
from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        # ! sol1: BFS and it's recommended
        if not root:
            return []

        result = []
        q = deque([root])

        while q:
            level_size = len(q)
            level_max = float("-inf")

            for _ in range(level_size):
                curr_node = q.popleft()
                level_max = max(level_max, curr_node.val)

                if curr_node.left:
                    q.append(curr_node.left)
                if curr_node.right:
                    q.append(curr_node.right)
            result.append(level_max)

        return result


# @lc code=end


#
# @lcpr case=start
# [1,3,2,5,3,null,9]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3]\n
# @lcpr case=end

#
