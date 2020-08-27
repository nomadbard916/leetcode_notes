#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None

        while head:
            # find next node when current(head) and previous nodes are known
            next_node = head.next

            head.next = prev

            prev = head
            head = next_node

        return prev


# @lc code=end

