#
# @lc app=leetcode id=24 lang=python3
#
# [24] Swap Nodes in Pairs
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        # sanity check
        if head is None or head.next is None:
            return head

        # as final head is uncertain
        pre = dummy = ListNode()

        while head and head.next:
            next_node = head.next

            # assign next nodes for head, next_node and pre
            head.next, next_node.next, pre.next = next_node.next, head, next_node

            # go to next head
            pre, head = head, head.next

        return dummy.next


# @lc code=end

