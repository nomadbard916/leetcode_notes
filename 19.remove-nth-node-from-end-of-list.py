#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = fast = slow = ListNode()
        dummy.next = head

        # make the gap between fast and slow with fast starting first
        for _ in range(n + 1):
            fast = fast.next

        # move fast until reaching null node, thus guaranteeing the gap between fast and slow
        while fast is not None:
            fast = fast.next
            slow = slow.next

        # when slow is well positioned, just point the link to the correct node
        slow.next = slow.next.next

        return dummy.next


# @lc code=end
