#
# @lc app=leetcode id=589 lang=python3
# @lcpr version=30201
#
# [589] N-ary Tree Preorder Traversal
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
    def preorder(self, root: "Node") -> List[int]:
        if not root:
            return []

        # ! sol1: recursion
        res = []

        def helper(root):
            if not root:
                return
            res.append(root.val)
            for children in root.children:
                helper(children)

        helper(root)

        return res

        # ! sol2: iterative
        stack, output = [root], []
        while stack:
            root = stack.pop()
            output.append(root.val)
            # add the children of the temp into the stack in reverse order.
            # children of 1 = [3,2,4], if not reveresed then 4 will be popped out first from the stack.
            # if reversed then stack = [4,2,3]. Here 3 will pop out first.
            # This continues till the stack is empty.
            stack.extend(root.children[::-1])

        return output


# @lc code=end


#
# @lcpr case=start
# [1,null,3,2,4,null,5,6]\n
# @lcpr case=end

# @lcpr case=start
# [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]\n
# @lcpr case=end

#
