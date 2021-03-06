# @before-stub-for-debug-begin
from python3problem92 import *
from typing import *

# @before-stub-for-debug-end

#
# @lc app=leetcode id=92 lang=python3
#
# [92] Reverse Linked List II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        dummy = ListNode()

        # without recording it here, it may be lost if m == 1 as prev.next is not updated in the process
        dummy.next = head
        prev = dummy

        # looping to locate partial head and prev and memorize them
        for _ in range(1, m):
            prev, head = head, head.next

        before_reverse, first_reversed = prev, head

        # looping until just out of reverse range
        for _ in range(n - m + 1):
            head.next, prev, head = prev, head, head.next

        # reestablish links
        before_reverse.next, first_reversed.next = prev, head

        return dummy.next


# @lc code=end

