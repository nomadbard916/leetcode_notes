#
# @lc app=leetcode id=61 lang=python3
#
# [61] Rotate List
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        # see # 19 for comparison,
        # which is more imaginable but more complicated

        if head is None:
            return head

        list_length = 1

        head_for_length = head

        while head_for_length.next:
            head_for_length = head_for_length.next
            list_length += 1

        # make it circle so cutting only needs on new tail,
        # which is done later
        head_for_length.next = head

        # get real k, cutting value passing list_length
        k %= list_length

        before_cut = head

        for _ in range(list_length - k - 1):
            before_cut = before_cut.next

        new_head = before_cut.next
        before_cut.next = None

        return new_head


# @lc code=end

