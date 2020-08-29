from collections import deque

#
# @lc app=leetcode id=234 lang=python3
#
# [234] Palindrome Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head or not head.next:
            return True

        tmp_list = []
        while head:
            tmp_list.append(head.val)
            head = head.next

        l, r = 0, len(tmp_list) - 1

        while l < r:
            if tmp_list[l] != tmp_list[r]:
                return False
            l += 1
            r -= 1

        return True


# @lc code=end

