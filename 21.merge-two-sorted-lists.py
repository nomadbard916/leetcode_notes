#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # each node move 1 step at once
        dummy = ListNode()
        prev = dummy

        while l1 and l2:
            if l1.val > l2.val:
                prev.next = l2
                l2 = l2.next
            else:
                prev.next = l1
                l1 = l1.next

            prev = prev.next
        while l1:
            prev.next = l1
            l1 = l1.next
            prev = prev.next
        while l2:
            prev.next = l2
            l2 = l2.next
            prev = prev.next

        return dummy.next


# @lc code=end

