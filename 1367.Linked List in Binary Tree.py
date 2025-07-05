#
# @lc app=leetcode id=1367 lang=python3
# @lcpr version=30201
#
# [1367] Linked List in Binary Tree
#

# @lc code=start
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        def dfs(head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
            if not head:
                return True
            if not root:
                return False

            if head.val != root.val:
                return False

            return dfs(head.next, root.left) or dfs(head.next, root.right)

        if not head:
            return True
        if not root:
            return False

        return dfs(head.next, root.left) or dfs(head.next, root.right)


# @lc code=end


#
# @lcpr case=start
# [4,2,8]\n[1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]\n
# @lcpr case=end

# @lcpr case=start
# [1,4,2,6]\n[1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]\n
# @lcpr case=end

# @lcpr case=start
# [1,4,2,6,8]\n[1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]\n
# @lcpr case=end

#
