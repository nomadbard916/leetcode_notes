#
# @lc app=leetcode id=83 lang=python3
#
# [83] Remove Duplicates from Sorted List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        # head is certain, therefore memorize it for returning purpose
        initial_head = head

        while head:
            # only check the next node from currently traversed node
            if head.next and head.next.val == head.val:
                head.next = head.next.next
            else:
                head = head.next

        return initial_head


# @lc code=end

