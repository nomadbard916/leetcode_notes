#
# @lc app=leetcode id=109 lang=python3
#
# [109] Convert Sorted List to Binary Search Tree
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        # sanity check
        if head is None:
            return head

        pre_mid, slow, fast = None, head, head

        while fast and fast.next:
            fast = fast.next.next
            pre_mid = slow
            slow = slow.next

        if pre_mid:
            pre_mid.next = None

        mid = TreeNode(slow.val)

        if slow == fast:
            return mid

        mid.left = self.sortedListToBST(head)
        mid.right = self.sortedListToBST(slow.next)

        return mid


# @lc code=end

