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
        # process overview
        # 1. Visit every node in the binary tree (using isSubPath)
        # 2. For each tree node, ask: "Could the linked list path start from here?"
        # 3. To answer this, use DFS to check if values match going downward:
        # - Compare current tree node with current linked list node
        # - If they match, move to next linked list node and try both tree children
        # - If we reach the end of linked list → Success!
        # - If we reach dead end in tree but still have linked list nodes → Fail
        # 4. If any starting position works → return True
        # 5. If no starting position works → return False

        # Empty linked list is always a subpath
        if not head:
            return True
        # Empty tree cannot contain any subpath
        if not root:
            return False

        def dfs(head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
            # * Helper function to check if linked list matches a path starting from current tree node.
            # Reached end of linked list - found complete match
            if not head:
                return True
            # Reached end of tree path but still have linked list nodes
            if not root:
                return False

            # Current values must match AND rest of path must match
            if head.val != root.val:
                return False

            return dfs(head.next, root.left) or dfs(head.next, root.right)

        # Check if path starts from current node OR from left/right subtree
        return (
            dfs(head, root)
            or self.isSubPath(head, root.left)
            or self.isSubPath(head, root.right)
        )


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
