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

        dummy.next = head
        prev, curr = dummy, dummy.next

        # looping to locate partial head and prev and memorize them
        for _ in range(m - 1):
            prev, curr = curr, curr.next

        before_reverse, first_reversed = prev, curr

        for _ in range(n - m + 1):
            curr.next, prev, curr = prev, curr, curr.next

        # reestablish links
        before_reverse.next, first_reversed.next = prev, curr

        return dummy.next


# @lc code=end

