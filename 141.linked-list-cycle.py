#
# @lc app=leetcode id=141 lang=python3
#
# [141] Linked List Cycle
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        # initial state
        turtle = head
        hare = head

        # these two nodes are acting as traverser
        # need to do sanity check for hare.next as hare can be already None
        while turtle and hare and hare.next:
            turtle = turtle.next
            # sanity check should've been done here, but it's moved earlier to while loop condition
            hare = hare.next.next

            if turtle == hare:
                return True

        return False


# @lc code=end

