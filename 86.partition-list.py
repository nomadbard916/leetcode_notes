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
        before_node = dummy_before = ListNode()
        after_node = dummy_after = ListNode()

        # * traverse the linked list
        # find the heads of two lists and link them in the process
        while head:
            if head.val < x:
                before_node.next = head
                before_node = before_node.next
            # this list will contain the target
            else:
                after_node.next = head
                after_node = after_node.next

            head = head.next

        # * Finish by connecting the two lists and terminating the after list.
        after_node.next = None
        before_node.next = dummy_after.next

        return dummy_before.next


# @lc code=end
