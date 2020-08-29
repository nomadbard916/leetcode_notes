#
# @lc app=leetcode id=142 lang=python3
#
# [142] Linked List Cycle II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        seen = set()

        while head:
            if head not in seen:
                seen.add(head)
            else:
                return head

            head = head.next

        return None


# @lc code=end

