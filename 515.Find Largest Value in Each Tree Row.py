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

            # Process all nodes in current level
            for _ in range(level_size):
                curr_node = q.popleft()
                level_max = max(level_max, curr_node.val)

                # put children of current level to prepare for next level process
                if curr_node.left:
                    q.append(curr_node.left)
                if curr_node.right:
                    q.append(curr_node.right)

            result.append(level_max)

        return result

        # ! sol2: DFS with level recording
        if not root:
            return []

        result = []

        def dfs(node: Optional[TreeNode], level: int) -> None:
            if not node:
                return

            if level == len(result):
                result.append(node.val)
            else:
                result[level] = max(result[level], node.val)

            dfs(node.left, level + 1)
            dfs(node.right, level + 1)

        dfs(root, 0)

        return result

        # Time and Space Complexity:
        # Time Complexity: O(n) where n is the number of nodes (we visit each node exactly once)
        # Space Complexity:
        # BFS: O(w) where w is the maximum width of the tree (queue storage)
        # DFS: O(h) where h is the height of the tree (recursion stack)


# @lc code=end


#
# @lcpr case=start
# [1,3,2,5,3,null,9]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3]\n
# @lcpr case=end

#
