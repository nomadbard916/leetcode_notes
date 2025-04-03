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

    # def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
    #     # p1 指向 A 链表头结点，p2 指向 B 链表头结点
    #     p1, p2 = headA, headB
    #     while p1 != p2:
    #         # p1 走一步，如果走到 A 链表末尾，转到 B 链表
    #         p1 = p1.next if p1 else headB
    #         # p2 走一步，如果走到 B 链表末尾，转到 A 链表
    #         p2 = p2.next if p2 else headA
    #     return p1


# @lc code=end
