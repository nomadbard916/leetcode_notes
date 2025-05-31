#
# @lc app=leetcode id=590 lang=python3
# @lcpr version=30201
#
# [590] N-ary Tree Postorder Traversal
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""


class Solution:
    def postorder(self, root: "Node") -> List[int]:
        if not root:
            return []

        # ! sol1: recursive
        result = []

        def helper(root):
            if not root:
                return None
            for children in root.children:
                helper(children)
            # visit root after children are traversed
            result.append(root.val)

        helper(root)
        return result

        # ! sol2: iterative
        res = []
        stack = [root]
        while stack:
            node = stack.pop()
            if node is not None:
                res.append(node.val)
            for children in node.children:
                stack.append(children)
        return res[::-1]


# @lc code=end


#
# @lcpr case=start
# [1,null,3,2,4,null,5,6]\n
# @lcpr case=end

# @lcpr case=start
# [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]\n
# @lcpr case=end

#
