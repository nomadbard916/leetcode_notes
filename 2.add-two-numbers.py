#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # add each one and create list nodes  while traversing both linked lists
        # deal with carry when there's over 10
        # consider when l1 or l2 ends

        dummy_node = ListNode()
        prev_node = dummy_node

        carry = 0

        while l1 and l2:
            temp_sum = l1.val + l2.val + carry

            uncarry_sum = temp_sum % 10
            carry = int(temp_sum / 10)

            # ie currently produced new node
            prev_node.next = ListNode(uncarry_sum)
            prev_node = prev_node.next

            l1 = l1.next
            l2 = l2.next

        while l1:
            temp_sum = l1.val + carry

            uncarry_sum = temp_sum % 10
            carry = int(temp_sum / 10)

            prev_node.next = ListNode(uncarry_sum)
            prev_node = prev_node.next

            l1 = l1.next

        while l2:
            temp_sum = l2.val + carry

            uncarry_sum = temp_sum % 10
            carry = int(temp_sum / 10)

            prev_node.next = ListNode(uncarry_sum)
            prev_node = prev_node.next

            l2 = l2.next

        if carry > 0:
            prev_node.next = ListNode(carry)

        return dummy_node.next


# @lc code=end

