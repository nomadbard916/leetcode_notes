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

    #  sol 2
    # def detectCycle(self, head: ListNode):
    #     fast, slow = head, head
    #     while fast and fast.next:
    #         fast = fast.next.next
    #         slow = slow.next
    #         if fast == slow:
    #             break

    #     # 上面的代码类似 hasCycle 函数
    #     if not fast or not fast.next:
    #         # fast 遇到空指针说明没有环
    #         return None

    #     # 重新指向头结点
    #     slow = head

    #     # 快慢指针同步前进，相交点就是环起点
    #     while slow != fast:
    #         fast = fast.next
    #         slow = slow.next
    #     return slow


# @lc code=end
