#
# @lc app=leetcode id=328 lang=python3
#
# [328] Odd Even Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        # refer to # 86 for two list chaining

        # odd/even index follow the first one?
        # !! not meaning odd/even value
        # space O(1) -> in place
        # time O(N) -> traversing all the nodes once

        # sanity check for:
        # no node in list
        if not head:
            return head

        # initial head must be odd
        current_odd = head
        # then next node of head must be even
        current_even = current_odd.next

        # head of even list must be the initial even node
        even_head = current_even

        # as current_odd cannot be None for even list to attach onto, therefore even nodes are used for looping
        while current_even and current_even.next:
            current_odd.next = current_even.next
            current_odd = current_odd.next

            # as the first even node is already assigned, the traversal skips the first one, seeking the second next ones instead
            # the 'current_odd' here is actually already the next node
            current_even.next = current_odd.next
            current_even = current_even.next

        # attach even linked list onto the last node of odd list
        current_odd.next = even_head

        return head


# @lc code=end

