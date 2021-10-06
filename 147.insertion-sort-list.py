#
# @lc app=leetcode id=147 lang=python3
#
# [147] Insertion Sort List
#

# @lc code=start
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # sanity check
        if not head or not head.next:
            return head

        pre_dummy = ListNode()
        pre_dummy.next = head

        current_sorted_node = head

        while current_sorted_node.next:
            if current_sorted_node.val <= current_sorted_node.next.val:
                # just step forward
                current_sorted_node = current_sorted_node.next
            else:
                # temporarily take out the node to manipulate,
                # then cut and link the list immediately
                to_insert = current_sorted_node.next
                current_sorted_node.next = current_sorted_node.next.next

                # iterating from head everytime to find the proper insert place
                # set current pointer to dummy outsider
                current_unsorted_node = pre_dummy

                while (
                    current_unsorted_node.next
                    and current_unsorted_node.next.val <= to_insert.val
                ):
                    current_unsorted_node = current_unsorted_node.next
                # find the position to insert,
                # then link previous node's next to to_insert,
                # and to_next's next node to original previous node's next node
                to_insert.next = current_unsorted_node.next
                current_unsorted_node.next = to_insert

        return pre_dummy.next


# @lc code=end

