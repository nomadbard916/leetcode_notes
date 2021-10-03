#
# @lc app=leetcode id=148 lang=python3
#
# [148] Sort List
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        # able to sort with O(nlogn)=>merge sort
        # 1. cut list to two equal lists, using slow and fast pointer
        # 2. merge sorted lists, see 21. Merge Two Sorted Lists

        if not head or not head.next:
            return head

        pre, slow, fast = None, head, head
        while fast and fast.next:
            pre = slow
            slow = slow.next
            fast = fast.next.next

        pre.next = None
        l1 = self.sortList(head)
        l2 = self.sortList(slow)

        return self.mergeTwoLists(l1, l2)

    def mergeTwoLists(self, l1, l2) -> ListNode:
        dummy = ListNode()
        head = dummy

        while l1 and l2:
            if l1.val < l2.val:
                head.next = l1
                l1 = l1.next
            else:
                head.next = l2
                l2 = l2.next

            head = head.next

        head.next = l1 or l2

        return dummy.next


# @lc code=end

