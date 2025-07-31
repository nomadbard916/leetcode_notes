#
# @lc app=leetcode id=86 lang=python3
#
# [86] Partition List
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head: ListNode | None, x: int) -> ListNode | None:
        # refer to # 328 for odd even list chaining

        # * use dummy nodes as outsider starting point
        lt_head = dummy_lt = ListNode()
        gte_head = dummy_gte = ListNode()

        # * traverse the linked list
        # find the heads of two lists and link them in the process
        while head:
            if head.val < x:
                lt_head.next = head
                lt_head = lt_head.next
            # this list will contain the target
            else:
                gte_head.next = head
                gte_head = gte_head.next

            head = head.next

        # * Finish by connecting the two lists and terminating the after list.
        gte_head.next = None
        lt_head.next = dummy_gte.next

        return dummy_lt.next


# @lc code=end
