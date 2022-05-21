#
# @lc app=leetcode id=24 lang=python3
#
# [24] Swap Nodes in Pairs
#

# @lc code=start
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=Optional[ListNode]):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        # * don't be tricked by the example.
        # the goal is to swap "in pair". don't consider swapping 4 nodes in once.

        # sanity check: head and head.next should be considered in pair
        if head is None or head.next is None:
            return head

        # as final head is uncertain
        pre = dummy = ListNode()
        dummy.next = head

        while head and head.next:
            next_node = head.next

            # assign next nodes for head, next_node and pre
            head.next = next_node.next
            next_node.next = head
            pre.next = next_node

            # go to next head
            pre, head = head, head.next

        return dummy.next


# @lc code=end
