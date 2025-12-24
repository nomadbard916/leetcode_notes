#
# @lc app=leetcode id=25 lang=python3
# @lcpr version=30201
#
# [25] Reverse Nodes in k-Group
#

# @lc code=start
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # nouns and verbs
        """
        linked list
        reverse every group of k
        * leave remainder as is
        """

        # pattern kws
        """
        linked list
        not alter - in place
        reverse
        * k-group - fixed size chunks, need counter for tracking group boundaries
        dummy node
        prev, tail, next_group_start
        reverse sublist, head insertion, iterative reversal
        """

        # structural kws
        """
        * exactly k nodes -> group size validation
        less than k nodes -> edge case handling
        positive integer
        not multiplier -> remain as is
        k at most 5000, relatively small
        val at most 1000, relatively small
        O(1) extra memory?

        """

        # mental categories
        """
        linked list manipulation
        """

        # build solution from keywords
        """
        * think of "reverse linked list" first, than add layers of orchestration
        1. use dummy node to handle edge cases
        2. count or look-ahead to verify k nodes exist
        3. reverse k nodes using standard reversal pattern
        4. connect reversed group back to main list
        5. move pointers to next group
        6. repeat until insufficient nodes remain
        """

        def get_kth_node(curr: Optional[ListNode], k: int) -> Optional[ListNode]:
            while curr and k > 0:
                curr = curr.next
                k -= 1
            return curr

        if not head or k == 1:
            return head

        dummy = ListNode(0)
        dummy.next = head

        prev_group_end = dummy

        while True:
            kth_node = get_kth_node(prev_group_end, k)

            if not kth_node:
                break

            next_group_start = kth_node.next

            prev, curr = kth_node.next, prev_group_end.next

            while curr != next_group_start:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            original_group_start = prev_group_end.next
            prev_group_end.next = kth_node

            prev_group_end = original_group_start

        return dummy.next


# @lc code=end


#
# @lcpr case=start
# [1,2,3,4,5]\n2\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4,5]\n3\n
# @lcpr case=end

#
