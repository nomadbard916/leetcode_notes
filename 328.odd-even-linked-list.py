#
# @lc app=leetcode id=328 lang=python3
#
# [328] Odd Even Linked List
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        # refer to # 86 for two list chaining

        # space O(1) -> in place
        # time O(N) -> traversing all the nodes once

        # sanity check for: no node in list => odd linked list must exist
        if not head:
            return head

        # initial head must be odd
        curr_odd = head
        # then next node of head must be even
        curr_even = curr_odd.next

        # head of even list must be the initial even node
        even_head = curr_even

        # as current_odd cannot be None for even list to be attached onto,
        # even nodes are used for looping
        while curr_even and curr_even.next:
            curr_odd.next = curr_even.next
            curr_odd = curr_odd.next

            # as the first even node is already assigned, traversal skips it,
            # instead seeking the next ones , i.e. starting from current_even.next
            # the 'current_odd' here is actually already the next node
            curr_even.next = curr_odd.next
            curr_even = curr_even.next

        # attach even linked list onto the last node of odd list
        curr_odd.next = even_head

        return head


# @lc code=end
