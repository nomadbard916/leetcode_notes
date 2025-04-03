#
# @lc app=leetcode id=160 lang=python3
#
# [160] Intersection of Two Linked Lists
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(
        self, headA: ListNode | None, headB: ListNode | None
    ) -> ListNode | None:
        # the final overlapping nodes must be equal,
        # therefore stack should be used as container when traversing linked lists
        stackA, stackB = [], []

        # put traversal results into stacks
        while headA:
            stackA.append(headA)
            headA = headA.next

        while headB:
            stackB.append(headB)
            headB = headB.next

        pre_node = None

        while stackA and stackB:
            topA, topB = stackA.pop(), stackB.pop()

            if topA != topB:
                return pre_node
            else:
                pre_node = topA

        return pre_node


# @lc code=end
