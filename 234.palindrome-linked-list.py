from collections import deque
from typing import Optional

#
# @lc app=leetcode id=234 lang=python3
#
# [234] Palindrome Linked List
#


# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        # ! sol1: optimal and complicated
        # 1. find the middle
        # 2. reverse second half
        # 3. compare
        def reverse_linked_list(head: Optional[ListNode]) -> Optional[ListNode]:
            prev = None
            curr = head

            while curr:
                next_tmp = curr.next
                curr.next = prev
                prev = curr
                curr = next_tmp

            return prev

        if not head or not head.next:
            return True

        slow: Optional[ListNode] = head
        fast: Optional[ListNode] = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second_half = reverse_linked_list(slow)
        first_half = head

        while second_half:
            if first_half.val != second_half.val:
                return False
            first_half = first_half.next
            second_half = second_half.next

        return True

        # ! sol2: convert linked list to array, then check with two pointers
        # easier to understand, but uses unnecessary extra space
        values = []

        current = head
        while current:
            values.append(current.val)
            current = current.next

        left, right = 0, len(values) - 1

        while left < right:
            if values[left] != values[right]:
                return False
            left += 1
            right -= 1

        return True


# @lc code=end
