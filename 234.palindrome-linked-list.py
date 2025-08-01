from collections import deque

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
