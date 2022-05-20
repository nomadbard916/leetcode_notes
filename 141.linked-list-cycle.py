#
# @lc app=leetcode id=141 lang=python3
#
# [141] Linked List Cycle
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        # initial state for two pointer
        turtle = head
        hare = head

        # these two nodes are acting as traverser
        # need to do sanity check for hare.next as hare can be already None
        while turtle and hare and hare.next:
            turtle = turtle.next
            # sanity check should've been done here,
            # but it's moved earlier to while loop condition
            hare = hare.next.next

            if turtle == hare:
                return True

        return False

        # sol2: just iterate and check if the current object is already seen
        # but it's with O(n) space complexity, compared to sol1's O(1)
        # seen: dict = {}
        # while head:
        #     if id(head) in seen:
        #         return True
        #     else:
        #         seen[id(head)] = True

        #     head = head.next

        # return False


# @lc code=end
