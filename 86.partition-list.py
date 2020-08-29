#
# @lc app=leetcode id=86 lang=python3
#
# [86] Partition List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        before_node = dummy_before = ListNode()
        after_node = dummy_after = ListNode()

        while head:
            if head.val < x:
                before_node.next = head
                before_node = before_node.next
            else:
                after_node.next = head
                after_node = after_node.next

            head = head.next

        after_node.next = None
        before_node.next = dummy_after.next

        return dummy_before.next


# @lc code=end

