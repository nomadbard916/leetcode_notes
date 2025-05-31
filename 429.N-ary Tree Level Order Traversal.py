#
# @lc app=leetcode id=429 lang=python3
# @lcpr version=30201
#
# [429] N-ary Tree Level Order Traversal
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

from collections import deque
from typing import List


class Solution:
    def levelOrder(self, root: "Node") -> List[List[int]]:
        if not root:
            return []

        q = deque()
        q.append(root)

        res = []

        while q:
            q_size = len(q)
            temp = []
            for _ in range(q_size):
                curr_node = q.popleft()
                temp.append(curr_node.val)
                if curr_node.children:
                    q.extend(curr_node.children)
            res.append(temp)
        return res


# @lc code=end


#
# @lcpr case=start
# [1,null,3,2,4,null,5,6]\n
# @lcpr case=end

# @lcpr case=start
# [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]\n
# @lcpr case=end

#
