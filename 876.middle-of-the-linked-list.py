#
# @lc app=leetcode id=876 lang=python3
#
# [876] Middle of the Linked List
#

# @lc code=start
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        turtle, hare = head, head
        # when hare reaches tail with 2x speed,
        # the travelling distance of turtle must be half of hare,
        # i.e. the middle of linked list
        while hare and hare.next:
            turtle = turtle.next
            hare = hare.next.next

        # if there's even nodes, there will be two middle nodes
        # the "turtle" returned is the latter node

        return turtle


# @lc code=end
