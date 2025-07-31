#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self, l1: ListNode | None, l2: ListNode | None
    ) -> ListNode | None:
        # it's outside and in front of all nodes
        dummy = ListNode()

        # starting from outsider dummy node
        curr_head = dummy

        while l1 and l2:
            if l1.val > l2.val:
                curr_head.next = l2
                l2 = l2.next
            else:
                curr_head.next = l1
                l1 = l1.next

            curr_head = curr_head.next
        while l1:
            curr_head.next = l1
            l1 = l1.next
            curr_head = curr_head.next
        while l2:
            curr_head.next = l2
            l2 = l2.next
            curr_head = curr_head.next

        return dummy.next


# @lc code=end
