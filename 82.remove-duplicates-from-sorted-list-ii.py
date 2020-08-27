#
# @lc app=leetcode id=82 lang=python3
#
# [82] Remove Duplicates from Sorted List II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import DefaultDict


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        # head is uncertain -> use dummy node

        # sanity check
        if head is None or head.next is None:
            return head

        dummy = ListNode()
        prev = dummy

        while head:
            prev.next = head

            # move head to the last one of duplicates
            while head.next and head.val == head.next.val:
                head = head.next

            # there are duplicates between head and prev
            if prev.next != head:
                prev.next = head.next
            # head is right next to prev
            else:
                prev = prev.next

            # finally head can move to next node and check again for duplicates
            head = head.next

        return dummy.next


# @lc code=end

